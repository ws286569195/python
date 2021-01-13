from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_httpauth import HTTPBasicAuth 
from flask_cors import CORS 

app = Flask(__name__) 
# flask的跨域解决 CORS(app) 
app.config.from_object('config') 
db = SQLAlchemy(app) 
auth = HTTPBasicAuth() 
from . import models, views