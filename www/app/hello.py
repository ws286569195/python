from flask import Flask
from mysql import DB
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/chaxun', methods=['POST', 'GET'])
def chaxun():
    qyxq =''
    if request.method == 'POST':
        qymc=request.form['qymc']
        with DB(host='127.0.0.1',user='root',passwd='aisino2017',db='xpf') as db:
            db.execute("select * from clientinfo where qymc like '%%%s%%'"%(qymc))
            #print(db)cd 
            qyxq=[]
            j=0
            for i in db:
                qyxq.append(i)
                j=j+1
                print(qyxq)
    return render_template('chaxun.html', qyxq=qyxq)


if __name__ == '__main__':
    app.run(debug=True)