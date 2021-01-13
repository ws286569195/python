# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
app = Flask("my-app")
CORS(app, resources=r'/*')


@app.route('/', methods=['POST'])
def hello_world():
    with DB(host='47.240.87.56', user='123', passwd='AHbTSiAYZMhG3jPy', db='test') as db:
        sql = "select * from userinfo"
        rows_count = db.execute(sql)
        if rows_count > 0:
            res = db.fetchall()
            return jsonify(res), 200
    return 'Hello World!'


@app.route('/choujiang', methods=['post'])  # 提供抽奖查询接口
def choujiang():
    print(request.headers)
    code = request.json.get('code')
    with DB(host='www.ted1988.com', user='123', passwd='AHbTSiAYZMhG3jPy', db='test') as db:
        if code == "001":
            sql = "select number,name,company from userinfo where qdbz = 1 and zjbz = 0"
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                return jsonify(res), 200
        elif code == "002":  # 搜索客户信息
            print(request.json.get('data'))
            data = request.json.get('data')
            # data = list(filter(None, data))
            for item in data:
                sql = "update userinfo set zjbz='%s' where number='%s'" % (item["zjbz"], item["number"])
                try:
                    db.execute(sql)
                except:
                    pass
            return jsonify(msg="00"), 200
        elif code == "003":  # 搜索客户信息
            sql = "select * from userinfo where zjbz <> 0"
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                return jsonify(res), 200
        elif code == "004":  # 重置抽奖标志
            sql = "UPDATE userinfo set zjbz =0"
            try:
                db.execute(sql)
            except:
                pass
        return jsonify(msg="00"), 200
@app.route('/research', methods=['post'])  # 提供查询接口
def research():
    print(request.headers)
    code = request.json.get('code')
    with DB(host='www.ted1988.com', user='123', passwd='AHbTSiAYZMhG3jPy', db='test') as db:
        if code == "001":
            sql = "select * from userinfo"
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                return jsonify(res), 200
        elif code == "002":  # 搜索客户信息
            number = request.json.get('number')
            sql = "select * from userinfo where number = '%s'" % number
            print(sql)
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                print(res)
                return jsonify(res), 200
            else:
                return jsonify(msg='104'), 200
        elif code == "003":  # 签到
            number = request.json.get('number')
            sql = "update userinfo set qdbz = 1 where number ='%s'" % number
            print(sql)
            try:
                # 执行sql语句
                db.execute(sql)
                # 提交到数据库执行
                # print(request.json.get('data'))
                return jsonify(msg="00"), 200
            except:
                # 发生错误时回滚
                # db.rollback()
                return jsonify(msg="01"), 200
        elif code == "004":  # 导入客户信息
            print(request.json.get('data'))
            data = request.json.get('data')
            for item in data:
                print("item")
                ls = {k: v for k, v in item.items() if v is not None}
                ls = {k: v for k, v in item.items() if v != ''}
                print(ls)
                sql = "INSERT INTO userinfo (number,name,phone,company,fzr,qdbz,zjbz)VALUES ('%s','%s','%s','%s','%s',0,0)" % (
                    ls.get('number', ''), ls.get('name', ''), ls.get('phone', ''), ls.get('company', ''), ls.get('fzr', ''))
                print(sql)
                try:
                    # 执行sql语句
                    db.execute(sql)
                    # 提交到数据库执行
                    # print(request.json.get('data'))
                except:
                    # 发生错误时回滚
                    # db.rollback()
                    return jsonify(msg="01"), 200
            return jsonify(msg="00"), 200
        elif code == "005":  # 修改客户信息
            print(request.json.get('data'))
            data = request.json.get('data')
            ls = {k: v for k, v in data.items() if v is not None}
            ls = {k: v for k, v in data.items() if v != ''}
            print(ls)
            # data = list(filter(None, data))
            sql = "update userinfo set name='%s',phone='%s',company='%s',fzr='%s',qdbz='%s',bz='%s' where number='%s'" % (
                ls.get('name', ''), ls.get('phone', ''), ls.get('company', ''), ls.get('fzr', ''), ls.get('qdbz', ''), ls.get('bz', ''), ls.get('number', ''))
            print(sql)
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
        elif code == "006":  # 删除客户信息
            print(request.json.get('data'))
            data = request.json.get('data')
            print(len(data))
            if len(data) == 1:
                sql = "delete from userinfo where number = '%s'" % data[0]["number"]
                print(sql)
            else:
                sql = "delete from userinfo where number in ("
                a = ""
                for item in data:
                    a = a + "'" + item["number"] + "',"
                sql = sql + a.rstrip(",") + ")"
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
        elif code == "007":  # 新增客户信息
            print(request.json.get('data'))
            data = request.json.get('data')
            sql = "INSERT INTO userinfo (number,name,phone,company,fzr,qdbz,zjbz)VALUES ('%s','%s','%s','%s','%s',1,0)" % (
                data.get('number', ''), data.get('name', ''), data.get('phone', ''), data.get('company', ''), data.get('fzr', ''))
            print(sql)
            try:
                # 执行sql语句
                db.execute(sql)
                return jsonify(msg="00"), 200
                # 提交到数据库执行
                # print(request.json.get('data'))
            except:
                # 发生错误时回滚
                # db.rollback()
                return jsonify(msg="01"), 200
        elif code == "008":  # 搜索客户名称
            name = request.json.get('name')
            sql = "select * from userinfo where name like '%%%s%%'" % name
            print(sql)
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                print(res)
                return jsonify(res), 200
            else:
                return jsonify(msg='104'), 200
        elif code == "009":  # 搜索客户电话
            phone = request.json.get('phone')
            sql = "select * from userinfo where phone like '%%%s%%'" % phone
            print(sql)
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                print(res)
                return jsonify(res), 200
            else:
                return jsonify(msg='104'), 200
        elif code == "010":  # 搜索客户公司
            company = request.json.get('company')
            sql = "select * from userinfo where company like '%%%s%%'" % company
            print(sql)
            rows_count = db.execute(sql)
            if rows_count > 0:
                res = db.fetchall()
                print(res)
                return jsonify(res), 200
            else:
                return jsonify(msg='104'), 200
class DB():
    def __init__(self, host='47.240.87.56', port=3306, db='', user='root', passwd='AHbTSiAYZMhG3jPy', charset='utf8'):
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
    app.run(host='0.0.0.0', port=5000, debug=True)
