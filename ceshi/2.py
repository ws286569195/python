# coding=utf-8
from tkinter import *
import tkinter as tk  #创建底层窗口
win=tk.Tk()
win.geometry("360x250")#控制窗口大小
win.title("窗口功能展示区")

#副窗口底层（手机号）
global a
def sj ():
    win1=tk.Toplevel()
    win1.geometry("800x300")
    win1.title("手机归属地查询窗口")
    #副窗口输入手机号标签展示
    lab=tk.Label(win1,fg="black",font="Helvetica 12 bold",text="输入手机号码")
    lab.grid(padx="20",pady="20")
    labelVar = tk.StringVar()
    global entry
    entry=tk.Entry(win1,font="Helvetica 15 bold",borderwidth=2,textvariable = labelVar)
    entry.grid()
    entry.pack(padx="30",pady="25")
    global a
    a=entry.get()
    print(a)
    #print(self.labelVar)
    qd=tk.Button(win1,text="确认",command=phone)
    qd.grid(padx="35",pady="25")
    win1.mainloop()

def phone():
    global a
    number=a
    print('111111'+a)
        
#主窗口按钮模块设置区
b1=tk.Button(win,width=30,text="1.手机号归属地查询",command=sj)
b1.grid(column=0,row=0)
b2=tk.Button(win,width=30,text="2.天气预报查询      ")
b2.grid(column=0,row=1)
b3=tk.Button(win,width=30,text="3.物业开票信息查询")
b3.grid(column=0,row=2)
b4=tk.Button(win,width=30,text="4.AES加解密         ")
b4.grid(column=0,row=3)
b5=tk.Button(win,width=30,text="5.退出                 ")
b5.grid(column=0,row=4)

#主窗口标签说明设置区
label=tk.Label(win,bg="#ffff00",fg="#ff0000",font="Helvetica 15 bold",padx=20,pady=5,text="仅限学术交流，禁止用于商业用途")
label.grid(column=0,row=5)
label=tk.Label(win,fg="#ff0000",font="Helvetica 10 bold",padx=20,pady=5,text="BY:小强制作")
label.grid(column=0,row=6)
win.mainloop()