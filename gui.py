#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import process
top = Tk()

def helloCallBack():
	inp=E1.get();
	correct=process.proc(inp);
	var.set(correct)
	

B = Button( text ="Submit", command = helloCallBack)
B.grid(row=2, column=0);


L1=Label(top,text="enter any word for suggeestion")
L1.grid(row=0,column=0)

E1 = Entry(top, bd =5)
E1.grid(row=1, column=0)


label = Label( top, text="correct version", relief=RAISED )
label.grid(row=3,column=0)

var=StringVar()
label = Label( top, textvariable=var, relief=RAISED )
var.set("");
label.grid(row=3,column=1)


top.mainloop()
