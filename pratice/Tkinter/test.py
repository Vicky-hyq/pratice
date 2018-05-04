#!/usr/bin/python
# coding:utf-8

from Tkinter import *

root = Tk()
#设置窗口的标题
root.title('Hello world')
#设置窗口的大小
root.geometry()
#标签

'''
Label(root,text='校训',font=("Arial", 15)).pack()

#在屏幕上创建一块矩形区域，多作为容器来布局窗体
frm = Frame(root)

frm_L = Frame(frm)
Label(frm_L,text='厚德',font=('Arial',12)).pack(side=TOP)
Label(frm_L,text='博学',font=('Arial',12)).pack(side=TOP)
frm_L.pack(side=LEFT)

frm_R =Frame(frm)
Label(frm_R,text='敬业',font=('Arial',12)).pack(side=TOP)
Label(frm_R,text='乐群',font=('Arial',12)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

root.mainloop()  #进入消息循环
'''

#创建单行文本框
var = StringVar()
e = Entry(root,textvariable = var)
var.set('')
e.pack()
root.mainloop()  #进入消息循环
