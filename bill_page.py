from tkinter import *
from tkinter import messagebox
import datetime 
from tkinter import ttk
import mysql.connector as sql
from customer_page import *
import os

global mycon,cur,income_table
mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
cur=mycon.cursor()
now = datetime.datetime.now()
months = ["","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
year = (now.year)
month = (months[now.month])
income_table='income_{}_{}'.format(month,year)
total_income='total_income_{}'.format(year)
def savebill():
    if messagebox.askquestion('CONFIRM','You want to print bill?')=='yes':
        now = datetime.datetime.now()
        today = datetime.date.today()
        d1 = today.strftime("%d/%m/%Y")
        time=str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        lineadd='\n\n\n'
        lineadd+="===============================================\n"
        lineadd+="                              Date : %s\n" % d1
        lineadd+="                              Time : %s\n\n" % time
        lineadd+="                 METRO MARKET\n"
        lineadd+="-----------------------------------------------\n"
        lineadd+="Name    : %s\n" % q1.get()
        lineadd+="Phone No: %s\n" % q2.get()
        lineadd+="-----------------------------------------------\n"
        lineadd+="Product                      Qty.       Price\n"
        lineadd+="-----------------------------------------------\n"
        for i in tree.get_children():
            f=tree.item(i)
            f=f['values']
            s1=' '
            s1=str(f[2]) + (s1 * (27-len(str(f[2])))) + s1*(3-len(str(f[3]))) +str(f[3])+ s1*(15-len(str(f[6])))+str(f[6]) + '\n'
            lineadd+=s1
        lineadd+="\n-----------------------------------------------\n"
        lineadd+='Total'+(' '*25)+(' '*(12-len(str(gtotal)))) +'Rs. '+ str(gtotal)+'\n'   
        lineadd+="-----------------------------------------------\n\n"
        lineadd+="Dealer 's signature:___________________________\n"
        lineadd+="===============================================\n"
        sql1='update {} set monthly_income=monthly_income+{}'.format(income_table,gtotal)
        sql1='update {} set total_income=total_income+{}'.format(total_income,gtotal)
        v=[sql1,sql2]
        for i in v:
            cur.execute(i)
            mycon.commit()
        bill=open('bill.txt','w')
        bill.write(lineadd)
        bill.close()
        os.startfile("bill.txt", "print")
    res1()
def check1():
    ph=n2.get()
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    cur.execute('select * from customer')
    r=cur.fetchall()
    if ph!='':
        for i in r:
            if ph==i[0]:
                n1.insert(0,i[1])
                break
        else:
            if messagebox.askquestion('ALERT','Customer Not Found. Do you want to add new customer?')=='yes':
               root2.destroy()
               customer_up_and_add('register','','','','')
               bill_page1()
    else:
        messagebox.showinfo('ALERT','No Phone Number entered!')
    mycon.close()
def sp():
    for i in range(c):
        l1.delete(0,END)
    sql1=''
    w1=q3.get()
    w2=q4.get()
    if w1!='' and w2=='':
        sql1='select * from stock where product_code="{}"'.format(w1)
    elif w1=='' and w2!='':
        sql1='select * from stock where product_name like "%{}%"'.format(w2)
    elif w1!='' and w2!='':
        sql1='select * from stock where product_code="{}" and product_name like "{}%"'.format(w1,w2)
    else:
        messagebox.showinfo('ALERT','Enter Product Details to search')
    if sql1!='':
        cur.execute(sql1)
        r=cur.fetchall()
        for i in r:
            l1.insert(END,i[1])
def ad1():
    global c,gtotal
    if l1.curselection():
        val=str((l1.get(ACTIVE)))
        r1=q5.get()
        sql1='select quantity from stock where product_name="{}"'.format(val)
        cur.execute(sql1)
        a1=cur.fetchone()
        a1=a1[0]
        if r1!='':
            if int(r1)<=int(a1):
                sql1='select * from stock where product_name="{}"'.format(val)
                cur.execute(sql1)
                r=cur.fetchall()
                r=r[0]
                if r[9]!='':
                    r2=r[9].rstrip('%')
                    total=int(r1)*int(r[4])
                    dis=total/int(r2)
                    total=total-dis
                else:
                    total=int(r1)*int(r[4])
                tree.insert("",'end',values=(c,r[0],r[1],r1,r[4],r[9],total))
                c=c+1
                gtotal+=total
                to.configure(text=gtotal)
                sql1='update stock set quantity=quantity-{} where product_code="{}"'.format(str(r1),str(r[0]))
                cur.execute(sql1)
                mycon.commit()
                for i in range(c):
                    l1.delete(0,END)
                m3.delete(0,END)
                m1.delete(0,END)
                m2.delete(0,END)
            else:
                q='OUT OF STOCK! current avilability of {} is {}'.format(val,a1)
                messagebox.showinfo('ALERT',q)
        else:
            q='Enter Quantity of '+val
            messagebox.showinfo('ALERT',q)    
    else:
        messagebox.showinfo('ALERT','No Product selected for adding to cart!')
def reg1():
    root2.destroy()
    customer_up_and_add('register','','','','')
    bill_page1()
def delete1():
    global c,gtotal
    if tree.focus():
        c1=tree.focus()
        f=tree.item(c1)
        f=f['values']
        ask='Do you want to remove "{}"?'.format(f[2])
        if messagebox.askquestion('CONFIRM',ask)=='yes':
            f1=f[0]
            f2=f[6]
            f3=f[3]
            f4=f[1]
            selected_item=tree.selection()[0]
            tree.delete(selected_item)
            x=tree.get_children()
            x1=x[f1-1:]
            for item in x1:
                f=tree.item(item)
                f=f['values']
                tree.item(item, values=(f1,f[1],f[2],f[3],f[4],f[5],f[6]))
                f1=f1+1
            c=c-1
            gtotal=gtotal-float(f2)
            sql1='update stock set quantity=quantity+'+str(f3)+' where product_code="'+str(f4)+'"'
            cur.execute(sql1)
            mycon.commit()
            to.configure(text=gtotal)
def res1():
    global c,gtotal
    m1.delete(0,END)
    m2.delete(0,END)
    m3.delete(0,END)
    n1.delete(0,END)
    n2.delete(0,END)
    for i in range(c):
        l1.delete(0,END)
    tree.delete(*tree.get_children())
    c=1
    gtotal=0
    to.configure(text=gtotal)
def res():
    if messagebox.askquestion('ALERT','DO you want to refresh the page') == 'yes':
        res1()
def viewde():
    pp=str((l1.get(ACTIVE)))
    if pp!='':
        sql1='select * from stock where product_name="{}"'.format(pp)
        cur.execute(sql1)
        r=cur.fetchone()
        tp=Toplevel(root2)
        tp.title('STOCK DETAILS')
        Label(tp,text='Product Code').grid(row=0,column=0)
        Label(tp,text=':').grid(row=0,column=1)
        Label(tp,text=r[0]).grid(row=0,column=3)
        Label(tp,text='Product Name').grid(row=1,column=0)
        Label(tp,text=':').grid(row=1,column=1)
        Label(tp,text=r[1]).grid(row=1,column=3)
        Label(tp,text='Manufactured By').grid(row=2,column=0)
        Label(tp,text=':').grid(row=2,column=1)
        Label(tp,text=r[2]).grid(row=2,column=3)
        Label(tp,text='Quantity').grid(row=3,column=0)
        Label(tp,text=':').grid(row=3,column=1)
        Label(tp,text=r[3]).grid(row=3,column=3)
        Label(tp,text='Unit Price').grid(row=4,column=0)
        Label(tp,text=':').grid(row=4,column=1)
        Label(tp,text=r[4]).grid(row=4,column=3)
        Label(tp,text='Supplier').grid(row=5,column=0)
        Label(tp,text=':').grid(row=5,column=1)
        Label(tp,text=r[5]).grid(row=5,column=3)
        Label(tp,text='Date Of Manufacture').grid(row=6,column=0)
        Label(tp,text=':').grid(row=6,column=1)
        Label(tp,text=r[6]).grid(row=6,column=3)
        Label(tp,text='Expiry Date').grid(row=7,column=0)
        Label(tp,text=':').grid(row=7,column=1)
        Label(tp,text=r[7]).grid(row=7,column=3)
        Label(tp,text='Category').grid(row=8,column=0)
        Label(tp,text=':').grid(row=8,column=1)
        Label(tp,text=r[8]).grid(row=8,column=3)
        Label(tp,text='Discount').grid(row=9,column=0)
        Label(tp,text=':').grid(row=9,column=1)
        Label(tp,text=r[9]).grid(row=9,column=3)
def bill_page1():
    today = datetime.date.today()
    d1 = today.strftime("%d/%m/%Y")
    global q1,q2,q3,q4,q5,n1,n2,n3,root2,l1,c,tree,gtotal,to,m1,m2,m3
    root2=Tk()
    gtotal=0
    c=1
    root2.geometry('1204x624')
    root2.resizable(0, 0)
    root2.title('   BILL PAGE')
    q1=StringVar()
    q2=StringVar()
    q3=StringVar()
    q4=StringVar()
    q5=StringVar()
    lf22=Frame(root2,bg='red',height=600,width=600)
    lf22.place(x=0,y=0)
    lf2=LabelFrame(lf22,text='DETAILS',font=15)
    lf2.pack(fill='both')
    Label(lf2,text='Date:').grid(row=0,column=0)
    Label(lf2,text=d1).grid(row=0,column=1)
    Label(lf2,text='Name').grid(row=1,column=0)
    n1=Entry(lf2,bd=3,width=30,textvariable=q1)
    n1.grid(row=1,column=1)
    Label(lf2,text='Phone No    ').grid(row=2,column=0)
    n2=Entry(lf2,bd=2,width=30,textvariable=q2)
    n2.grid(row=2,column=1)
    Button(lf2,text='CHECK PHONE NUMBER',command=check1).grid(row=3,columnspan=2)
    Button(lf2,text='ADD CUSTOMER',command=reg1).grid(row=4,columnspan=2)
    lf3=LabelFrame(lf22,text='SEARCH',font=15)
    lf3.pack(fill='both')
    Label(lf3,text='Product Id').grid(row=0,column=0)
    m1=Entry(lf3,bd=3,width=30,textvariable=q3)
    m1.grid(row=0,column=1)
    Label(lf3,text='Product Name').grid(row=1,column=0)
    m2=Entry(lf3,bd=3,width=30,textvariable=q4)
    m2.grid(row=1,column=1)
    Button(lf3,text='SEARCH',width=10,command=sp).grid(row=3,columnspan=2)
    Label(lf3,text='Products').grid(row=4,columnspan=2)
    l1=Listbox(lf3,height=21,width=55,bd=3)
    l1.grid(row=5,columnspan=3)
    Button(lf3,text='ADD PRODUCT',width=12,command=ad1).grid(row=6,column=0)
    Label(lf3,text='Quantity').place(x=145,y=440)
    m3=Entry(lf3,bd=2,width=20,textvariable=q5)
    m3.place(x=200,y=440)
    photo = PhotoImage(file = "images\\removeproduct.ico")
    Button(root2,image=photo,bd=0,command=delete1).place(x=360,y=530)    
    photo1 = PhotoImage(file = "images\\checkdetails.ico")
    Button(root2,image=photo1,bd=0,command=viewde).place(x=380,y=577)
    photo2 = PhotoImage(file = "images\\print_bill.ico")
    Button(root2,image=photo2,bd=0,command=savebill).place(x=610,y=530)
    photo3 = PhotoImage(file = "images\\reset-bill.ico")
    Button(root2,image=photo3,bd=0,command=res).place(x=610,y=577)    
    Label(root2,text='|\n|\n|\n|\n|\n|\n|\n|\n|').place(x=790,y=520)
    photo6 = PhotoImage(file = "images\\grandtotal.png")
    photo6=photo6.subsample(2,2)
    Label(root2,image=photo6).place(x=880,y=530)
    to=Label(root2,text='0',fg='blue',font=('arial',20))
    to.place(x=995,y=575)
    tree=ttk.Treeview(root2,height=25)
    tree.place(x=345,y=0)
    tree['columns']=('-1','0','1','2','3','4','5')
    tree['show']='headings'
    tree.heading('-1',text='S.No.')
    tree.heading('0',text='Product Code')
    tree.heading('1',text='Product Name')
    tree.heading('2',text='Quantity')
    tree.heading('3',text='Unit Price')
    tree.heading('4',text='Discount')
    tree.heading('5',text='Total Price')
    tree.column('4',width=100,anchor='center')
    tree.column('3',width=100,anchor='center')
    tree.column('2',width=100,anchor='center')
    tree.column('1',width=210,anchor='center')
    tree.column('5',width=100,anchor='center')
    tree.column('-1',width=80,anchor='center')
    tree.column('0',width=164,anchor='center')
    root2.mainloop()

