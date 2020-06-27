from tkinter import *
from tkinter import ttk

GUI = Tk() #นี่คือหน้าต่างหลักของโปรแกรม
GUI.geometry('500x300') #ปรับขนาด
GUI.title('ตัวอย่าง') #หัวข้อ Title
################FUNCTION################

def ExpenseRice():
    print('คุณมีค่าใช้จ่าย: ข้าว ราคา 25 บาท')
def ExpenseCofee():
    print('คุณมีค่าใช้จ่าย: กาแฟ ราคา 50 บาท')
def ExpenseTaxi():
    print('คุณมีค่าใช้จ่าย: ค่าแท็กซี่ ราคา 35 บาท')






################ROW1################

F1 = Frame(GUI) # F1 คือ เฟรม (White board ติดผนัง)
F1.place(x=20, y=20) #.place คือการกำหนดตำแหน่ง

B1 = ttk.Button(F1, text='ข้าว', command=ExpenseRice)
B1.grid(row=0, column=0, ipadx=20, ipady=10, padx=5)
#pady=10 คือ การทำให้มีระยะห่างแนว บน,ล่าง 10 pixel


B2 = ttk.Button(F1, text='กาแฟ', command=ExpenseCofee)
B2.grid(row=0, column=1, ipadx=20, ipady=10, padx=5)


B3 = ttk.Button(F1, text='ค่าแท็กซี่', command=ExpenseTaxi)
B3.grid(row=0, column=2, ipadx=20, ipady=10, padx=5)

################ROW2################

F2 = Frame(GUI) # F1 คือ เฟรม (White board ติดผนัง)
F2.place(x=20, y=70) #.place คือการกำหนดตำแหน่ง

B1 = ttk.Button(F2, text='น้ำอัดลม')
B1.grid(row=0, column=0, ipadx=20, ipady=10, padx=5)
#pady=10 คือ การทำให้มีระยะห่างแนว บน,ล่าง 10 pixel


B2 = ttk.Button(F2, text='ผัก')
B2.grid(row=0, column=1, ipadx=20, ipady=10, padx=5)


B3 = ttk.Button(F2, text='ผงซักฟอก')
B3.grid(row=0, column=2, ipadx=20, ipady=10, padx=5)

GUI.mainloop() #ทำให้โปรแกรมรันตลอดเวลา
