from tkinter import *
import mysql.connector as sql
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
cur=mycon.cursor()
def validate(date_string):
    date_format = '%Y-%m-%d'
    try:
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def sub(*event):
            sq='select product_code from stock'
            cur.execute(sq)
            r=cur.fetchall()
            p1=pc.get()
            p2=pn.get()
            p3=mb.get()
            p4=qn.get()
            p5=up.get()
            p6=sd.get()
            p7=ed.get()
            p8=dm.get()
            p9=c.get()
            p10=dt.get()
            sql1=None
            if p1!='' and p2!='' and p4!='' and p5!='':
                try:
                    if p9!='other':
                        if p7!='' and p8!='':
                            if validate(p7):
                                if validate(p8):
                                    sql1 = "INSERT INTO stock(product_code,product_name,Man_by,quantity,unit_price,supplier,Date_of_man,expiry_date,category,discount) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                    val=(p1,p2,p3,p4,p5,p6,p8,p7,p9,p10)
                                else:
                                    messagebox.showinfo('ALERT','Enter valid Manufacture date in "YYYY-MM-DD" format',icon='warning')
                            else:
                                messagebox.showinfo('ALERT','Enter valid Expiry date in "YYYY-MM-DD" format',icon='warning')
                        else:
                            messagebox.showinfo('ALERT','Enter expiry date and manufacture date',icon='warning')
                    else:
                        if validate(p8):
                            sql1 = "INSERT INTO stock(product_code,product_name,Man_by,quantity,unit_price,supplier,Date_of_man,category,discount) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            val=(p1,p2,p3,p4,p5,p6,p8,p9,p10)
                        else:
                            messagebox.showinfo('ALERT','Enter Manufacture date in "YYYY-MM-DD" format',icon='warning')
                    if sql1:        
                        cur.execute(sql1, val)
                        mycon.commit()
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)
                        e6.delete(0,END)
                        e7.delete(0,END)
                        e8.delete(0,END)
                        e9.delete(0,END)
                        e10.delete(0,END)
                except sql.IntegrityError:
                    messagebox.showinfo('AlERT','product code already exists')
            else:
                messagebox.showinfo('ALERT','Product code,Product Name,Quantity,Unit price should not be empty',icon='warning')
def delete_info(*event):
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        p1=str(f[0])
        s='delete from stock where product_code = "'+p1+'"'
        cur.execute(s)
        mycon.commit()
        for i in tree.get_children():
            tree.delete(i)
        cur.execute('select * from stock')
        r=cur.fetchall()
        total=len(r)
        labl.configure(text=total)
        for i in r:
            tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
        mycon.close()
def re():
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    cur.execute('select * from stock')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
    mycon.close()
def search1():
    s=s1.get()
    if s!='':
        sql1='select * from stock where product_name like "%{}%"'.format(s)
        mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
        cur=mycon.cursor()
        cur.execute(sql1)
        r=cur.fetchall()
        total=len(r)
        if total!=0:
            labl.configure(text=total)
            for j in tree.get_children():
                tree.delete(j)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
            search2.delete(0,END)
        else:
            te="NO records found with name "+s
            messagebox.showinfo('ALERT',te)
    else:
        messagebox.showinfo('ALERT','No Name Specified for searching')
    mycon.close()
def back5():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        vm.destroy()
        stock_page()
def view1():
    try:
        r4.destroy()
    except:
        pass
    global tree,labl,s1,search2,vm
    cur.execute('select * from stock')
    r=cur.fetchall()
    vm=Tk()
    vm.title('STOCK DETAILS')
    vm.resizable(0,0)
    vm.geometry('1200x650')
    s1=StringVar()
    Tm = Frame(vm, width=600, bd=1, relief=SOLID)
    Tm.pack(side=TOP, fill=X)
    Lm = Frame(vm, width=300)
    Lm.pack(side=LEFT, fill=Y)
    Mm = Frame(vm, width=600)
    Mm.pack(side=RIGHT)
    text = Label(Tm, text="View Stock Details", font=('arial', 18), width=600)
    text.pack(fill=X)
    txtsearch = Label(Lm, text="Search name", font=('arial', 20)).place(x=70,y=50)
    search2 = Entry(Lm, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "images\\search.png")
    search = Button(Lm,image=photo,bd=0,command=search1).place(x=70,y=150)
    photo3 = PhotoImage(file = "images\\delete.png")
    delete = Button(Lm,image=photo3,bd=0,command=delete_info).place(x=70,y=230)
    photo4 = PhotoImage(file = "images\\reset.png")
    delete = Button(Lm,image=photo4,bd=0,command=re).place(x=60,y=310)
    photo5 = PhotoImage(file = "images\\back.png")
    delete = Button(Lm,image=photo5,bd=0,command=back5).place(x=80,y=390)
    scrollbarx = Scrollbar(Mm, orient=HORIZONTAL)
    scrollbary = Scrollbar(Mm, orient=VERTICAL)
    tree = ttk.Treeview(Mm, columns=('1','2','3','4','5','6','7','8','9','10'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4','5','6','7','8','9','10')
    tree['show']='headings'
    tree.heading('1', text="Product code")
    tree.heading('2', text="Product Name")
    tree.heading('3', text="Manufactured By")
    tree.heading('4', text="quantity")
    tree.heading('5', text="Unit Price")
    tree.heading('6', text="Supplier")
    tree.heading('7', text="Date Of Manufacture")
    tree.heading('8', text="Expiry Date")
    tree.heading('9', text="Category")
    tree.heading('10', text="Discount")
    tree.column('4',width=170,anchor='center')
    tree.column('3',width=280,anchor='center')
    tree.column('2',width=280,anchor='center')
    tree.column('1',width=170,anchor='center')
    tree.column('5',width=280,anchor='center')
    tree.column('6',width=280,anchor='center')
    tree.column('7',width=280,anchor='center')
    tree.column('8',width=280,anchor='center')
    tree.column('9',width=280,anchor='center')
    tree.column('10',width=280,anchor='center')
    tree.pack()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
    total=len(r)
    Label(vm,text='TOTAL RESULTS FOUND : ',font=('arial',14)).place(x=40,y=510)
    labl=Label(vm,text=total,font=('arial',25))
    labl.place(x=140,y=550)
    vm.mainloop()    

def back4():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        r3.destroy()
        stock_page()
def sto_reg():
    try:
        r4.destroy()
    except:
        pass
    global pc,pn,mb,qn,up,sd,ed,dm,c,dt,r3,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    r3=Tk()
    r3.title('STOCK ENTRY')
    r3.geometry('1220x630')
    r3.resizable(0,0)
    load = Image.open("images\\w1232.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(r3, image=render)
    img.image = render
    img.place(x=-230,y=0)
    pc=StringVar()
    pn=StringVar()
    mb=StringVar()
    qn=StringVar()
    up=StringVar()
    sd=StringVar()
    ed=StringVar()
    dm=StringVar()
    c=StringVar()
    dt=StringVar()
    photo3 = PhotoImage(file = "images\\stockimg.png")
    Label(r3,image=photo3,bg='#EDECF4').place(x=250,y=50)
    Label(r3,text='Product Code',font=('arial',13),bg='#EDECF4').place(x=360,y=220)
    e1=Entry(r3,textvariable=pc,font=('arial',13),bd=3,width=30)
    e1.place(x=470,y=220)
    Label(r3,text='Product Name',font=('arial',13),bg='#EDECF4').place(x=360,y=280)
    e2=Entry(r3,textvariable=pn,font=('arial',13),bd=3,width=30)
    e2.place(x=470,y=280)
    Label(r3,text='Manufactured \nBy',font=('arial',13),bg='#EDECF4').place(x=353,y=340)
    e3=Entry(r3,textvariable=mb,font=('arial',13),bd=3,width=30)
    e3.place(x=470,y=340)
    Label(r3,text='Quantity',font=('arial',13),bg='#EDECF4').place(x=370,y=400)
    e4=Entry(r3,textvariable=qn,font=('arial',13),bd=3,width=30)
    e4.place(x=470,y=400)
    Label(r3,text='Unit Price',font=('arial',13),bg='#EDECF4').place(x=370,y=460)
    e5=Entry(r3,textvariable=up,font=('arial',13),bd=3,width=30)
    e5.place(x=470,y=460)
    Label(r3,text='Supplier',font=('arial',13),bg='#EFEEF6').place(x=800,y=220)
    e6=Entry(r3,textvariable=sd,font=('arial',13),bd=3,width=30)
    e6.place(x=910,y=220)
    Label(r3,text='Date Of\n manufacture',font=('arial',13),bg='#EDECF4').place(x=780,y=276)
    e7=Entry(r3,textvariable=dm,font=('arial',13),bd=3,width=30)
    e7.place(x=910,y=280)
    Label(r3,text='Expiry Date',font=('arial',13),bg='#EDECF4').place(x=790,y=340)
    e8=Entry(r3,textvariable=ed,font=('arial',13),bd=3,width=30)
    e8.place(x=910,y=340)
    Label(r3,text='Category',font=('arial',13),bg='#EDECF4').place(x=795,y=400)
    e9=ttk.Combobox(r3,values=['Beverages','Bakery','Diary products','Frozen foods','Paper goods','Other'],textvariable=c,width=23,font=('arial',14))
    e9.place(x=910,y=400)
    Label(r3,text='Discount',font=('arial',13),bg='#EDECF4').place(x=795,y=460)
    e10=Entry(r3,textvariable=dt,font=('arial',13),bd=3,width=30)
    e10.place(x=910,y=460)
    photo = PhotoImage(file = "images\\submit.png")
    butt=Button(r3,image=photo,bd=0,activebackground='#EDECF4',bg='#EDECF4',command=sub)
    butt.place(x=720,y=500)
    photo2 = PhotoImage(file = "images\\back.png")
    butt=Button(r3,image=photo2,bd=0,activebackground='#EDECF4',bg='#EDECF4',command=back4)
    butt.place(x=740,y=570)
    r3.mainloop()  
def stock_page():
    global r4
    r4=Tk()
    r4.title('STOCK PAGE')
    r4.resizable(0,0)
    r4.geometry('1200x650')
    load = Image.open("images\\w103.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(r4, image=render)
    img.image = render
    img.place(x=0,y=0)
    photo3 = PhotoImage(file = "images\\stockdet.png")
    Label(r4,image=photo3,bg='#EF8367').place(x=100,y=100)
    photo4 = PhotoImage(file = "images\\addstock.png")
    Button(r4,image=photo4,bg='#E87A61',bd=0,activebackground='#E87A61',command=sto_reg).place(x=220,y=280)
    photo5 = PhotoImage(file = "images\\editstock.png")
    Button(r4,image=photo5,bd=0,bg='#E5775E',activebackground='#E5775E',command=view1).place(x=220,y=410)
    r4.mainloop()
stock_page()
