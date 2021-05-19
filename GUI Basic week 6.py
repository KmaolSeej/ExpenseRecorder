# GUI-การบ้าน.py

"""การบ้าน
-------
สร้างช่องกรอกจำนวน แล้วคำนวณค่า total แล้วบันทึกเป็นข้อมูล
data = [‘น้ำเต้าหู้’,20,3,60]
data = [ชื่อรายการ, ราคา, จำนวน, รวมทั้งหมด]

extra: ถ้าทำได้ให้บันทึกเวลาตอนเซฟด้วย
คำใบ้: 
from datetime import datetime
dt = datetime.now()
"""


from tkinter import *
from tkinter.ttk import Notebook
from tkinter import ttk, messagebox
from datetime import datetime
import csv


GUI = Tk()
GUI.title('Program บันทึกค่าใช้จ่าย by ลุงปลอม Ver.2')
GUI.geometry('500x600+500+50') #แนวแกน X,Y จากมุมซ้ายบน
#B1 = Button(GUI,text='Hello')
#B1.pack(ipadx=50,ipady=20) # ติดปุ่มเข้าไปกับ GUI หลัก(internal padding ความใหญ่pixel)
FONT1 = ('Times New Roman',18) #เปลี่ยนFont 'Angsana New'
FONT2 = ('Times New Roman',10)

#########  Menubar #####################
menubar = Menu(GUI)
GUI.config(menu=menubar)

#File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='inport CSV')
filemenu.add_command(label='Export to googlesheet')

def About():
	messagebox.showinfo('About', 'สวัสดีครับ\n สวัสดี')
#Help
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)



#Donate
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)


##############################


Tab = ttk.Notebook(GUI)
T1 = ttk.Frame(Tab)
T2 = ttk.Frame(Tab)

expenseicon = PhotoImage(file='expense.png').subsample(14)
listicon = PhotoImage(file='list.png').subsample(6)
Tab.pack(fill= BOTH ,expand=1)

Tab.add(T1, text=f'{"Add Expense":^{20}}',image=expenseicon,compound='top')
Tab.add(T2, text=f'{"Expense List": ^20s}',image=listicon,compound='top')

F1=Frame(T1)
F1.pack()

F2=Frame(T2)
F2.pack()



#Dictionary
days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}



def Save(event=None):
	expense = v_expense.get()   #ดึงค่ามาจาก v_expense = StringVar()
	price = v_price.get()
	amount = v_amount.get()

	if expense == '':
		print('No Data')
		messagebox.showinfo('Error','กรุณากรอกข้อมูลให้ครบ')
		return
	elif price =='':
		print('No Data')
		messagebox.showinfo('Error','กรุณากรอกราคา')
		return
	elif amount =='':
		amount = 1
		#print('No Data')
		#messagebox.showinfo('Error','กรุณากรอกจำนวน')
		#return	

	total = float(price)*float(amount)
	try:
		total = float(price)*float(amount)
		today = datetime.now().strftime('%a') #days=['Mon'] = 'จันทร์'
		# print(today)
		dt1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		dt1 = days[today] + '-' + dt1
		print('รายการ: {} ราคา: {} จำนวน: {} รวมมูลค่า: {} วัน: {} '.format(expense,price,amount,total,dt1))
		#textshow = 'รายการ: {} บาท/รายการ\n จำนวน: {} รายการ\n รวมมูลค่า: {} บาท\n เวลา: {} '.format(expense,price,amount,total,dt)
		#messagebox.showinfo('บันทึกค่าใช้จ่าย',textshow)
		text = 'รายการ: {}\n ราคา: {}\n'.format(expense,price)
		text = text + 'จำนวน: {}\n รวมมูลค่า: {}\n วัน: {}\n '.format(amount,total,dt1)
		v_result.set(text)

				   
		#Clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_amount.set('')
		
		#บันทึกข้อมูลลง CSV อย่างลืม Import ลง CSV ด้วย
		with open('savedataHW.csv','a',encoding='UTF-8',newline='') as f:
			#with เปิดไฟล์แล้วปิดอัตโนมัติ
			# 'a' การบันทึกเพิ่มข้อมูลไปเรื่อยๆต่อจากข้อมูลเก่า (แต่ 'w' เขียนใหม่ทั้งหมด)
			# newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง 
			fw = csv.writer(f) #สร้างฟังก์ชันสำหรับเขียนข้อมูล
			data = [expense,price,amount,total,dt1]
			fw.writerow(data)
		
			

		E1.focus()#ทำให้ Curser กลับไปตำแหน่งช่องกรอก E1
		update_table()
	except Exception as e:

		print('ERROR',e)
		#messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ กรอกเฉพาะตัวเลข')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ กรอกเฉพาะตัวเลข')
		#messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ กรอกเฉพาะตัวเลข')

		v_expense.set('') #Clear ข้อมูลเก่า
		v_price.set('')
		v_amount.set('')








# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

#--------Background 1------------
bg = PhotoImage(file='account.png').subsample(1)
acpic = ttk.Label(F1, image=bg)
acpic.pack(pady=1)


#-----text1-------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย', font=FONT1).pack()
v_expense = StringVar() #StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI

E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()

#-----text2-------
L = ttk.Label(F1,text='ราคา(บาท)', font=FONT1).pack()
v_price = StringVar() 

E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()

#-----text3-------
L = ttk.Label(F1,text='จำนวน', font=FONT1).pack()
v_amount = StringVar() 

E3 = ttk.Entry(F1,textvariable=v_amount,font=FONT1)
E3.pack()



saveicon = PhotoImage(file='save.png').subsample(8)
B2 = ttk.Button(F1,image=saveicon,text=f'{"SAVE":^{10}}',command=Save,compound='top')
B2.pack(ipadx=20,ipady=10,pady=10) #ติดปุ่มเข้าไปกับ GUI (ใช้ ipadไม่ได้)


v_result =StringVar()
v_result.set('-------ผลลัพธ์-------')
result = ttk.Label(F1,textvariable=v_result,font=FONT2,foreground='blue')
result.pack(pady=10)


############### Tab 2 ###############
# rs=[]

def read_csv():
	# global rs
	with open('savedataHW.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
		rs = data
		# print(rs)
	return data
# print(data)
		# print('--------')
		# print(data[0][0])
		# for a,b,c,d,e in data:
		# 	print(b)

# rs = read_csv()
# print(rs[0]) 

#table
L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด', font=FONT1).pack(pady=5)
header = ['รายการ','ราคา','จำนวน','รวมยอด','วัน-เวลา']
resulttable = ttk.Treeview(T2, columns=header,show='headings',heigh=10)
resulttable.pack(pady=20)

# for i in range(len(header)):
# 	resulttable.heading(header[i],text=header[i])

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [130,50,50,50,180]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)

# resulttable.insert('','end',value=[1,2,3,4,5])

def update_table():
	resulttable.delete(*resulttable.get_children())
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)
	# print(data)


update_table()
print('GET CHILD:',resulttable.get_children())
GUI.bind('<Tab>',lambda x: E2.focus()) #ดูว่ามีการกดปุ่ม enter หรือเปล่า ถ้ามีก็เหมือนรัน Save จึงต้องต้องเพิ่มใน def Save(event=None) ด้วย 
GUI.mainloop()
#เป็นการ Run ตลอดเวลา GUI สมบูรณ์ เช็คตลอดว่ามีใครกดปุ่มอะไรหรือยัง
