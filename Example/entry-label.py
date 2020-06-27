#entry-label.py

from tkinter import *
from tkinter import ttk

GUI = Tk() #นี่คือหน้าต่างหลักของโปรแกรม
GUI.geometry('500x300') #ปรับขนาด
GUI.title('ตัวอย่าง') #หัวข้อ Title

E1 = ttk.Entry(GUI, text='ข้าว')
E1.pack(pady=20)


GUI.mainloop() #ทำให้โปรแกรมรันตลอดเวลา
