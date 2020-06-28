from tkinter import *
from tkinter import ttk

GUI = Tk() #นี่คือหน้าต่างหลักของโปรแกรม
GUI.title('ตัวอย่าง') #หัวข้อ Title

w = 700
h = 500

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #ปรับขนาด
#GUI.state('zoomed')


GUI.mainloop() #ทำให้โปรแกรมรันตลอดเวลา
