#GUIExpense.py

from tkinter import *
from tkinter import ttk
#########CSV##########
import csv

#Comma-separated values: CSV

def WritetoCSV(ep):
    with open('allexpense.csv','a',newline='',encoding='utf-8') as file:
        # 'a' = append (เพิ่มได้เรื่อยๆ) , 'w' = replace (ทับไฟล์เดิม)
        fw = csv.writer(file) # fw คือ file writer
        # ep = ['ไก่',300]
        fw.writerow(ep)

    print('Done!')

def ReadCSV():
    with open('allexpense.csv',newline='',encoding='utf-8') as file:
        #fr = file reader
        fr = csv.reader(file)
        #print(list(fr))
        data = list(fr)
    return data

########MAIN GUI########
GUI = Tk() # นี่คือหน้าต่างหลักของโปรแกรม
GUI.title('ตัวอย่าง')
GUI.iconbitmap('wallet.ico')

w = 700
h = 600

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #ปรับขนาด
#GUI.state('zoomed')

menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Exit - (F4)',command=GUI.quit)
#command= lambda: GUI.destroy()
GUI.bind('<F4>',lambda x: GUI.destroy())

## helpmenu
import webbrowser

def About():
    url = 'https://www.uncle-engineer.com'
    webbrowser.open(url)

from tkinter import messagebox as msb

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)
helpmenu.add_command(label='Donate',command=lambda: msb.showinfo('Donate','เลขบัญชี: 700 258 444\nธนาคารกรุงไทย'))
#command=lambda: msb.showinfo('Donate','เลขบัญชี: 700 258 444\nธนาคารกรุงไทย')


from tkinter.ttk import Notebook

Tab = Notebook(GUI)
Tab.pack(fill=BOTH, expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_expense = PhotoImage(file='cart.png')
icon_income = PhotoImage(file='money.png')
icon_dashboard = PhotoImage(file='dashboard.png')

Tab.add(T1,text='รายจ่าย',image=icon_expense,compound='top')
Tab.add(T2,text='รายรับ',image=icon_income,compound='top')
Tab.add(T3,text='สรุปผล',image=icon_dashboard,compound='top')


####################Expense######################

FONT1 = ('Angsana New',15)
FONT2 = ('Angsana New',20,'bold')

# v_expense ใช้สำหรับเก็บค่าที่ user พิมพ์
v_expense = StringVar()

# E1 คือช่องกรอกข้อมูล
L = ttk.Label(T1,text='กรุณากรอกรายจ่าย').pack() #หัวข้อบนช่องกรอก
E1 = ttk.Entry(T1,textvariable=v_expense, font=FONT1, width=30)
E1.pack(pady=10)

# v_expense ใช้สำหรับเก็บค่าที่ user พิมพ์
v_price = StringVar()

# E1 คือช่องกรอกข้อมูล
L = ttk.Label(T1,text='ค่าใช้จ่าย (บาท)').pack() #หัวข้อบนช่องกรอก
E2 = ttk.Entry(T1,textvariable=v_price, font=FONT1, width=30)
E2.pack(pady=10)


# SaveExpense คือฟังชั่นเมื่อมีการกดปุ่ม ฟังชั่นนี้จะทำงาน
from datetime import datetime #เวลา

def SaveExpense(event=None):
    exp = v_expense.get()
    pc = float(v_price.get()) # แปลงข้อความเป็นจุดทศนิยม
    # ข้อความเป็นตัวเลขใช้ int() , ข้อความเป็นจุดทศนิยม float() , ตัวเลขหรือจุดทุศนิยมเป็นข้อความ str()
    print('รายการ: ',exp) # v_expense.get() คือการดึงค่ามาใช้งาน
    #v_result.set('คุณกำลังบันทึกรายการ: ' + exp + ' ราคา: '+ v_price.get() +' บาท')
    v_result.set(f'กำลังบันทึกรายการ: {exp} ราคา: {pc:,.2f} บาท')

    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = [dt,exp,pc] #จัดเรียงข้อมูลก่อนเซฟลง csv
    WritetoCSV(data) #เรียกฟังชั่นการบันทึกข้อมูล

    #reset ตัวแปร
    v_expense.set('')
    v_price.set('')
    #ทำให้ cursor วิ่งไปหาช่องกรอกตัวแรก
    E1.focus()
    update_table() #อัพเดตตารางทุกครั้งที่มีการเพิ่มรายการใหม่
    

E2.bind('<Return>',SaveExpense) #หากใช้ bind ต้องใส่ event=None ในฟังชั่นด้วย

# B1 คือปุ่มสำหรับกดบันทึก
B1 = ttk.Button(T1,text='บันทึก',command=SaveExpense)
B1.pack()

#######LABEL########
v_result = StringVar()
R1 = ttk.Label(T1, textvariable= v_result, font=FONT2, foreground='green') # R1 = Label(fg='green')
R1.pack(pady=20)

########Expense Button##########

expenselist = {'rice':{'name':'ข้าว','price':20},
               'coffee':{'name':'กาแฟ','price':25},
               'taxi':{'name':'ค่าแท็กซี่','price':35}}

###########FUNCTION########
def Expense(keyword):
    price = expenselist[keyword]['price']
    print('ค่าใช้จ่าย: ' + expenselist[keyword]['name'])
    print('ราคา: ',price)

    ep = expenselist[keyword]['name']
    
    v_expense.set(ep)
    v_price.set(price)

###########ROW1############

F1 = Frame(T1)# F1 คือ เฟรม (white board ติดผนัง)
F1.pack()

B1 = ttk.Button(F1,text='ข้าว',command=lambda x='rice': Expense(x))
B1.grid(row=0,column=0,ipadx=20,ipady=10,padx=5)
# pady=10 คือการทำให้มีระยะห่างแนวบนล่าง 10 พิกเซล

B2 = ttk.Button(F1,text='กาแฟ',command=lambda x='coffee': Expense(x))
B2.grid(row=0,column=1,ipadx=20,ipady=10,padx=5)

B3 = ttk.Button(F1,text='ค่าแท็กซี่',command=lambda x='taxi': Expense(x))
B3.grid(row=0,column=2,ipadx=20,ipady=10,padx=5)


#########TABLE###########

header = ['วัน-เวลา','รายการ','จำนวนเงิน']

table_expense = ttk.Treeview(T1,column=header,show='headings',height=20)
table_expense.pack(pady=20)

table_expense.heading('วัน-เวลา',text='วัน-เวลา')
table_expense.heading('รายการ',text='รายการ')
table_expense.heading('จำนวนเงิน',text='จำนวนเงิน')

def sum_table():
    allsum = []
    data = ReadCSV()
    for dt in data:
        #dt = [2020-06-27 17:00:03,ข้าว,20.0]
        allsum.append(float(dt[2]))
    v_allexpense.set('{:,.2f} บาท'.format(sum(allsum)))

def update_table():
    data = ReadCSV()
    print(data)
    table_expense.delete(*table_expense.get_children()) 
    #clear ข้อมูลทั้งหมดในตาราง ก่อนการ insert
    for dt in data:
        table_expense.insert('','end',value=dt)
    sum_table()

#อัพเดตรายการตอนรันครั้งแรก

v_allexpense = StringVar()

L = ttk.Label(T3,text='ยอดรวมทั้งหมด (บาท):',font=FONT1).place(x=50,y=50)
LR1 = ttk.Label(T3,textvariable=v_allexpense,font=FONT2)
LR1.place(x=200,y=45)

update_table()
GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลา