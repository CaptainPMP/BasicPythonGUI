Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("Hello World")
Hello World
>>> name = 'Robert'
>>> print(name)
Robert
>>> type(name)
<class 'str'>
>>> name.upper()
'ROBERT'
>>> from tkinter import *
>>> GUI = Tk()
>>> GUI.geometry('400x300')
''
>>> GUI.title('โปรแกรมบันทึกรายรับรายจ่าย')
''
>>> B1 = Button(GUI, text='Hello')
>>> B1.pack()
>>> E1 = Entry(GUI)
>>> E1.pack()
>>> L1 = Label(GUI, text='กรุณากรอกค่าใช้จ่าย')
>>> L1.pack()
>>> from tkinter import ttk
>>> B2 = ttk.Button(GUI, text='สวัสดี')
>>> B2.pack()
>>> E2 = ttk.Entry(GUI)
>>> E2.pack()
>>> L2 = ttk.Label(GUI, text='กรอกรายรับ')
>>> L2.pack()
>>> B3 = ttk.Button(GUI, text='บันทึก')
>>> B3.place(x=250,y=200)
>>> B3.place(x=100,y=200)
>>> 