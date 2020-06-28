from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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

F1 = Frame(GUI)
F1.place(x=250, y=20) #.place คือการกำหนดตำแหน่ง
F2 = Frame(GUI)
F2.place(x=250, y=60) #.place คือการกำหนดตำแหน่ง
F3 = Frame(GUI)
F3.place(x=250, y=100) #.place คือการกำหนดตำแหน่ง

##########################RADIO BUTTON#############################
v_radio = StringVar() #เก็บค่าจากการเลือก

RB1 = ttk.Radiobutton(F1, text='Pop up',variable=v_radio, value='popup')
RB2 = ttk.Radiobutton(F1, text='print',variable=v_radio, value='print')
RB1.grid(row=0, column=0)
RB2.grid(row=0, column=1)
RB1.invoke() #ทำให้ RB1 เป็นค่า Default

def Run():
	v = v_radio.get()
	print(v_radio.get()) #ดึงค่าจากตัวแปรที่เก็บค่าของ radio
	if v == 'popup':
		messagebox.showinfo('Popup', 'คุณกำลังเลือก Popup') #โชว์ข้อความแจ้งให้ทราบ
		#messagebox.showwarning('Popup', 'คุณกำลังเลือก Popup') #โชว์ข้อความแจ้งเตือน
		#messagebox.showerror('Popup', 'คุณกำลังเลือก Popup') #โชว์ข้อความมีปัญหา
	else:
		print('คุณไม่ได้เลือก popup คุณเลือก print')

B1 = ttk.Button(F1, text='Run', command=Run)
B1.grid(row=0, column=2, padx=20)

##########################RADIO BUTTON#############################


##########################CHECK BUTTON#############################

c1 = StringVar()
c1.set('ไม่เอาข้าว')#set ค่า default
c2 = StringVar()
c2.set('ไม่เอาปลา')
c3 = StringVar()
c3.set('น้ำดื่มมีแล้ว')

C1 = ttk.Checkbutton(F2, text='ข้าว', onvalue='ข้าว', offvalue='ไม่เอาข้าว',variable=c1)
C1.grid(row=0, column=0)

C2 = ttk.Checkbutton(F2, text='ปลา', onvalue='ปลา', offvalue='ไม่เอาปลา',variable=c2)
C2.grid(row=0, column=1)

C3 = ttk.Checkbutton(F2, text='น้ำดื่ม', onvalue='น้ำดื่ม', offvalue='ไม่เอาน้ำดื่ม',variable=c3)
C3.grid(row=0, column=2)



def SelectFood():
	print(c1.get())
	print(c2.get())
	print(c3.get())
	print('------')

B2 = ttk.Button(F2, text='Select Food', command=SelectFood)
B2.grid(row=0, column=3, padx=20)

##########################CHECK BUTTON#############################

###########################COMBO BOX###############################

cblist = ['บัตรเครดิต','เงินสด','โอน']

CB1 = ttk.Combobox(F3, values=cblist)
CB1.set('เงินสด')
CB1.grid(row=0, column=0)

def Dropdown():
	print(CB1.get())

B3 = ttk.Button(F3, text='Dropdown', command=Dropdown)
B3.grid(row=0, column=1, padx=20)

###########################COMBO BOX###############################

GUI.mainloop() #ทำให้โปรแกรมรันตลอดเวลา
