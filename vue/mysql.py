import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
app = Flask(__name__)
CORS(app, resources=r'/*')

# token私钥
app.config['JWT_SECRET_KEY'] = 'TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'
jwt = JWTManager(app)


@app.route('/')
def hello_world():
    return ""


@app.route("/api/login", methods=['POST'])  # 登录判断，成功返回token
def form_args():
    print(request.headers)
    print(request.json.get('username'))
    username = request.json.get('username')
    password = request.json.get('password')
    with DB(host='127.0.0.1', user='root', passwd='root', db='test') as db:
        sql = "select * from userinfo where username='%s'" % username
        rows_count = db.execute(sql)
        print(password)
        if rows_count > 0:
            for i in db:
                print(i['username']+"__"+i['password']+"__"+i['xingming'])
                if password == i['password']:
                    access_token = create_access_token(i['xingming'])
                    return jsonify(access_token=access_token, msg="登录成功"), 200
                else:
                    print("密码不匹配")
                    return jsonify(msg="密码错误"), 400
        else:
            print("未找到用户名")
            return jsonify(msg="用户名错误错误"), 400


@app.route('/research', methods=['post'])  # 提供查询接口
@jwt_required
def research():
    print(request.headers)
    code = request.json.get('code')
    with DB(host='127.0.0.1', user='root', passwd='root', db='test') as db:
        if code == "001":
            sql = "select * from clientinfo"
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                return jsonify(res), 200
        elif code == "002":  # 增加客户信息
            null = 'null'
            data = request.json.get('data')
            clientname = "'" + str(data['clientname']) + "'"
            if data['clienttax'] == "":
                clienttax = null
            else:
                clienttax = "'" + str(data['clienttax']) + "'"
            if data['clientaddress'] == "":
                clientaddress = null
            else:
                clientaddress = "'" + str(data['clientaddress']) + "'"
            if data['clientphone'] == "":
                clientphone = null
            else:
                clientphone = "'" + str(data['clientphone']) + "'"
            if data['clientbank'] == "":
                clientbank = null
            else:
                clientbank = "'" + str(data['clientbank']) + "'"
            if data['clientbankno'] == "":
                clientbankno = null
            else:
                clientbankno = "'" + str(data['clientbankno']) + "'"

            sql = "INSERT INTO clientinfo (clientname,clienttax,clientaddress,clientphone,clientbank,clientbankno)VALUES (%s,%s,%s,%s,%s,%s)" % (
                clientname, clienttax, clientaddress, clientphone, clientbank, clientbankno)
            print(request.json.get('data'))
            print(sql)
            try:
                # 执行sql语句
                db.execute(sql)
                # 提交到数据库执行
                # print(request.json.get('data'))
                return jsonify(msg="增加成功"), 200
            except:
                # 发生错误时回滚
                # db.rollback()
                return jsonify(msg="增加失败"), 200
        elif code == "003":  # 删除客户信息
            print(request.json.get('data'))
            data = request.json.get('data')
            print(len(data))
            if len(data) == 1:
                sql = "delete from clientinfo where id = %s" % str(
                    data[0]["ID"])
                print(sql)
            else:
                sql = "delete from clientinfo where id in ("
                index = 1
                a = ""
                for item in data:
                    a = a + str(item["ID"])
                    if index < len(data):
                        a = a+","
                        index += 1
                sql = sql + a + ")"
                print(sql)
            try:
                # 执行sql语句
                db.execute(sql)
                # 提交到数据库执行
                return jsonify(msg="删除成功"), 200

            except:
                # 发生错误时回滚
                # db.rollback()
                return jsonify(msg="删除失败"), 200
        elif code == "004":  # 修改客户信息
            print(request.json.get('data'))
            data = request.json.get('data')
            null = 'null'
            data = request.json.get('data')
            clientname = "'" + str(data['clientname']) + "'"
            if data['clienttax'] == None:
                clienttax = null
            else:
                clienttax = "'" + str(data['clienttax']) + "'"
            if data['clientaddress'] == None:
                clientaddress = null
            else:
                clientaddress = "'" + str(data['clientaddress']) + "'"
            if data['clientphone'] == None:
                clientphone = null
            else:
                clientphone = "'" + str(data['clientphone']) + "'"
            if data['clientbank'] == None:
                clientbank = null
            else:
                clientbank = "'" + str(data['clientbank']) + "'"
            if data['clientbankno'] == None:
                clientbankno = null
            else:
                clientbankno = "'" + str(data['clientbankno']) + "'"
            sql = "update clientinfo set clientname=%s,clienttax=%s,clientaddress=%s,clientphone=%s,clientbank=%s,clientbankno=%s where id=%d" % (
                clientname, clienttax, clientaddress, clientphone, clientbank, clientbankno, data["ID"])
            try:
                # 执行sql语句
                db.execute(sql)
                # 提交到数据库执行
                # print(request.json.get('data'))
                return jsonify(msg="修改成功"), 200
            except:
                # 发生错误时回滚
                # db.rollback()
                return jsonify(msg="修改失败"), 200


@app.route('/protected', methods=['post'])  # 带token验证的路由
@jwt_required
def protected():
    print(request.headers)
    return jsonify({'hello': 'world'}), 200


class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(
            host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    app.run()
