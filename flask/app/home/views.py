#coding:utf8
from . import home
from flask import render_template

@home.route("/home")
def index():
    return render_template("home/home.html",t="aaa")
@home.route("/")
def login():
    return render_template("home/login.html",t="aaa")
