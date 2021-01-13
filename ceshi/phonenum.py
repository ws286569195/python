from suds import Client
from tkinter import messagebox
import tkinter
def check(s):
    url = 'http://www.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
    d = Client(url)
    x = 1
    while x > 0:
        if s.isdigit():
            if int(s) < x:
                break
            if len(s) != 11:
                return('手机号位数不对！请重新输入')
                continue
            else:
                r = d.service.getMobileCodeInfo(s)
                print(r)
                n= r.split()
                n1=n[0].split("：")
                print(n)
                return(n)
                break
        else:
            return('输入的不全是数字！')
            continue
def helloCallBack(r):
    #tkinter.messagebox.showinfo( "结果", check(r))
    xianshi.insert('insert',check(r))
def gettext():
    text=t.get()
    helloCallBack(text)
top = tkinter.Tk()
top.geometry('500x300+500+200')
t = tkinter.Entry(top,width = 11,)
t.place(x=0,y=11,anchor='nw')
w = tkinter.Button(top,height = 1,width = 10,text = '查询', command = gettext)
w.place(x=250,y=200,anchor='nw')
xianshi = tkinter.Text(top,height = 5,width = 50)
xianshi.place(x=145,y=0,anchor='nw')
# 进入消息循环
top.mainloop()
