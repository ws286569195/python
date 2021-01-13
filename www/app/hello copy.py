from flask import Flask
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
        pass
if __name__ == '__main__':
    app.run(debug=True)