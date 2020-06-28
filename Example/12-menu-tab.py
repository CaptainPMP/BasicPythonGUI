from tkinter import *
from tkinter import ttk

GUI = Tk() #นี่คือหน้าต่างหลักของโปรแกรม
GUI.title('ตัวอย่าง') #หัวข้อ Title
GUI.iconbitmap('wallet.ico')

w = 700
h = 500

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #ปรับขนาด
#GUI.state('zoomed')

######################################################

menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Exit - (F4)',command=GUI.quit)
#MacOS -> command = lambda: GUI.destroy()

GUI.bind('<F4>',lambda x: GUI.destroy())

## Help menu
import webbrowser
def About():
	url = 'https://www.captainpmp.lnw.mn/'
	webbrowser.open(url)

from tkinter import messagebox as msb

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)
helpmenu.add_command(label='Donate', command=lambda: msb.showinfo('Donate','TrueWallet : 064-694-8060'))
#command=lambda: msb.showinfo('Donate','TrueWallet : 064-694-8060')


from tkinter.ttk import Notebook

Tab = Notebook(GUI)
Tab.pack(fill=BOTH, expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)


icon_expense = PhotoImage(file='cart.png')
icon_imcome = PhotoImage(file='money.png')
icon_dashboard = PhotoImage(file='dashboard.png')


Tab.add(T1,text='รายจ่าย', image=icon_expense,compound='top')
Tab.add(T2,text='รายรับ', image=icon_imcome,compound='top')
Tab.add(T3,text='สรุปผล', image=icon_dashboard,compound='top')

GUI.mainloop() #ทำให้โปรแกรมรันตลอดเวลา