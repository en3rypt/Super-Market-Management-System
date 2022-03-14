#============================== import statements================
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as sql
import random,string,smtplib,datetime,calendar
#============================MySQL COMMANDS========================
now = datetime.datetime.now()
months = ["","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
year = (now.year)
month = (months[now.month])
income_table='income_{}_{}'.format(month,year)
total_income='total_income_{}'.format(year)
mycon=sql.connect(host='localhost',user='root',passwd='root')
cur=mycon.cursor()
cur.execute('create database if not exists supermarket')
cur.execute('use supermarket')
cur.execute('create table if not exists login_info(l_type varchar(20), username varchar(50) primary key, password varchar(50))')
mycon.commit()
try:
    cur.execute('insert into login_info values("admin","admin","admin")')
    mycon.commit()
except:
    pass
try:
    sqla='create table {}(total_income int)'.format(total_income)
    sqlb='create table {}(monthly_income int)'.format(income_table)
    sqlc='insert into {} values(0) '.format(income_table)
    sqld='insert into {} values(0) '.format(total_income)
    val=[sqla,sqlb,sqlc,sqld]
    for i in val:
        cur.execute(i)
        mycon.commit()
except:
    pass
sqla=  'CREATE TABLE if not exists customer(phone_no varchar(20) primary key,Name varchar(50),address varchar(300),email varchar(60))'
sqlb = "CREATE TABLE if not exists  stock(product_code varchar(20) PRIMARY KEY, product_name varchar(100),Man_by varchar(100),quantity varchar(20),unit_price varchar(20),supplier varchar(100),Date_of_man varchar(20), expiry_date varchar(20),category varchar(20), discount varchar(10)) "
sqlc = "CREATE TABLE if not exists emp(emp_id varchar(20) PRIMARY KEY,first_name varchar(100),last_name varchar(100),D_O_B varchar(20),phone_no varchar(15),email varchar(100),qualification varchar(100),gender varchar(20),experience varchar(100),fathers_name varchar(100),mothers_name varchar(100),address varchar(300))"
val=[sqla,sqlb,sqlc]
for i in val:
    cur.execute(i)
    mycon.commit()
#=================================================================

from customer_page import *
from emp_re import *
from stock_pa import *
from bill_page import *
from income_page import *
#==================================================================
def back():
    r0.destroy()
    login()
def passwordreset():
    root.destroy()
    global r0
    r0=Tk()
    q1=StringVar()
    q11=StringVar()
    r0.title('RESET PASSWORD PAGE')
    r0.geometry('1200x650')
    ######### images ##############
    load = Image.open("images\\w90.jpg")
    photo9 = PhotoImage(file = "images\\resetpassword.png")
    photo = PhotoImage(file = "images\\resetpass.png")
    photo1 = PhotoImage(file = "images\\back.png")
    ###############################
    render = ImageTk.PhotoImage(load)
    img = Label(r0, image=render)
    img.image = render
    img.place(x=0,y=-50)
    def submitpassword():
        q=q1.get()
        sql1='select username from login_info where username="{}"'.format(q)
        cur.execute(sql1)
        r=cur.fetchone()
        if r:
            password=randomPassword()
            sql1='select email from emp where emp_id="{}"'.format(q)
            cur.execute(sql1)
            w=cur.fetchone()
            if w:
                passwd1=q11.get()
                email(w[0],r[0],passwd1)
            else:
                w='No email found for username {}'.format(q)
                messagebox.showinfo('Alert',w)
    Label(r0,image=photo9,bg='#EDF0F7').place(x=400,y=240)
    Label(r0,text='USERNAME',font=('arial',14),bg='#F0F8Fb').place(x=435,y=330)
    a1=Entry(r0,width=20,textvariable=q1,bd=3,font=('arial',13))
    a1.place(x=575,y=331)
    Label(r0,text='ADMIN PASSWORD',font=('arial',14),bg='#F0F8Fb').place(x=390,y=365)
    a1=Entry(r0,width=20,textvariable=q11,show='*',bd=3,font=('arial',13))
    a1.place(x=575,y=366)
    photo=photo.subsample(2,2)
    Button(r0,image=photo,bd=0,bg='#F0F4F7',activebackground='#F0F4F7',command=submitpassword).place(x=500,y=400) 
    Button(r0,image=photo1,bd=0,bg='#F0F4F7',activebackground='#F0F4F7',command=back).place(x=530,y=450)
    r0.mainloop()
# LOGIN PAGE
def login():
    global root
    root = Tk()
    root.geometry('1155x650+150+150')
    root.title('LOGIN PAGE')
    root.resizable(0,0)
    usr=StringVar()
    pwd=StringVar()
    ######### images ##############
    load = Image.open("images\\w43.jpg")
    photo3 = PhotoImage(file = "images\\logintext.png")
    photo1 = PhotoImage(file = "images\\l.ico")
    ###############################
    def check(*event):
        us=usr.get()
        pw=pwd.get()
        cur.execute('select * from login_info')
        r=cur.fetchall()
        for i in r:
            if i[1]==us and i[2]==pw:
                root.destroy()
                if i[0]=='admin':
                    return main_page(i[0])
                elif i[0]=='employee':
                    return main_page(i[0])  
        else:
            messagebox.showinfo('warning','incorrect username or password')
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=0,y=0)
    photo3=photo3.subsample(2,2)
    Label(root,image=photo3,bg='#D2E4E4').place(x=435,y=210)
    Label(root,text='USERNAME',font=('arial',14),bg='#D0E3E1').place(x=385,y=270)
    a1=Entry(root,width=20,bd=3,textvariable=usr,font=('arial',13))
    a1.place(x=507,y=274)
    Label(root,text='PASSWORD',font=('arial',14),bg='#D0E3E1').place(x=380,y=320)
    a2=Entry(root,width=20,bd=3,textvariable=pwd,show='*',font=('arial',13))
    a2.place(x=507,y=320)
    def change1(*event):
        a2.focus()
    a1.bind('<Return>',change1)
    a2.bind('<Return>',check)    
    photo1 = photo1.subsample(3,3)
    b1=Button(root,bd=0,command=check,activebackground='#D0E3E1',font=10,bg='#D0E3E1',image=photo1).place(x=460,y=350)
    Label(root,text='Forgot Password?',bg='#CCE0DF',font=('arial',13)).place(x=420,y=430)
    b2=Button(root,text='Reset Password',font=('arial',13,'underline'),activebackground='#D0E3E1',bd=0,bg='#CDE1E0',fg='blue',command=passwordreset).place(x=570,y=428)
    root.mainloop()
def randomPassword():
    randomSource = string.ascii_letters + string.digits 
    password = random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)
    for i in range(6):
        password += random.choice(randomSource)
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password
def email(q,user,passwd1):
    try:
        p=randomPassword()
        p2=str(p)
        q1='Your password is {}'.format(p2)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sanjiththirumuganathan@gmail.com", str(passwd1))
        server.sendmail("sanjiththirumuganathan@gmail.com",q,q1)
        sql1='update login_info set password="{}" where username="{}"'.format(p,user)
        cur.execute(sql1)
        mycon.commit()
        messagebox.showinfo('Alert','Mail successfully sent')
    except:
        c='Mail not sent to {}. please contact admin.'.format(q)
        messagebox.showinfo('Alert',c)
def main_page(user):
    root1 = Tk()
    root1.geometry('1200x650')
    root1.resizable(0, 0)
    def qui():
         if messagebox.askyesno('DONE','Do you want to log out?'):
            root1.destroy()
            login()
    def cc():
        root1.destroy()
        cus_page()
        main_page(user)
    def ee():
        root1.destroy()
        emp_page()
        main_page(user)
    def ss():
        root1.destroy()
        stock_page()
        main_page(user)
    def bb():
        root1.destroy()
        bill_page1()
        main_page(user)
    def mm():
        root1.destroy()
        main_income_page()
        main_page(user)
    ####### images ###############
    load = Image.open("images\\w83.jpg")
    photo4 = PhotoImage(file = "images\\bill.png")
    photo6 = PhotoImage(file = "images\\customer.png")
    photo5 = PhotoImage(file = "images\\sto.png")
    photo7 = PhotoImage(file = "images\\employee.png")
    photo8 = PhotoImage(file = "images\\viewin.png")
    photo9 = PhotoImage(file = "images\\logout.png")
    ##############################
    render = ImageTk.PhotoImage(load)
    img = Label(root1, image=render)
    img.image = render
    img.place(x=0,y=0)
    Label(root1,text='SUPER MARKET',bg='#eff0eb',fg='red',font=('times',33,'bold')).place(x=280,y=10)
    Label(root1,text='MANAGEMENT SYSTEM',bg='#e8E9E3',fg='red',font=('times',33,'bold')).place(x=644,y=10)
    Button(root1,image=photo4,bd=0,command=bb,bg='#E7E8E2',activebackground='#E7E8E2').place(x=550,y=100)
    Button(root1,image=photo6,bd=0,command=cc,bg='#E7E8E2',activebackground='#E7E8E2').place(x=500,y=190)
    Button(root1,image=photo5,bd=0,command=ss,bg='#E7E8E2',activebackground='#E7E8E2').place(x=535,y=280)
    if user=='admin':
        root1.title('ADMIN PAGE')
        Button(root1,image=photo7,bd=0,command=ee,bg='#E7E8E2',activebackground='#E7E8E2').place(x=500,y=370)
        c=Button(root1,image=photo8,bd=0,command=mm,bg='#E7E8E2',activebackground='#E7E8E2').place(x=570,y=460)
        Button(root1,image=photo9,command=qui,bd=0,bg='#E7E8E2',activebackground='#E7E8E2').place(x=605,y=550)
        Label(root1,text='logged in as Admin',bg='#E2E3DD',fg='red',font=('arial',20)).place(x=950,y=600)
    else:
        root1.title('EMPLOYEE PAGE')
        Button(root1,image=photo9,command=qui,bd=0,bg='#E7E8E2',activebackground='#E7E8E2').place(x=605,y=390)
        Label(root1,text='logged in as employee',bg='#E2E3DD',fg='red',font=('arial',20)).place(x=900,y=600)
    root1.mainloop()
login()



    
