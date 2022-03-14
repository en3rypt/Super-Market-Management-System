from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from tkinter import ttk
import random
import datetime
from PIL import Image, ImageTk
mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
cur=mycon.cursor()
def l_code():
    cur.execute('select * from emp')
    r=cur.fetchall()
    now = datetime.datetime.now()
    c='emp'
    a1=random.randint(0,26)
    c+=str(now.year)[2:]
    c+=str(100000+len(r))
    return c
def re():
    cur.execute('select * from emp')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
def search1():
    s=s1.get()
    if s!='':
        sql1='select * from emp where first_name like "{}%"'.format(s)
        cur.execute(sql1)
        r=cur.fetchall()
        total=len(r)
        if total!=0:
            labl.configure(text=total)
            for j in tree.get_children():
                tree.delete(j)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))
            search2.delete(0,END)
        else:
            te="NO records found with name {}".format(s)
            messagebox.showinfo('ALERT',te)
    else:
        messagebox.showinfo('ALERT','No Name Specified for searching')
def delete_info(*event):
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        p1=str(f[0])
        s='delete from emp where emp_id = "{}"'.format(p1)
        print(s)
        cur.execute(s)
        mycon.commit()
        for i in tree.get_children():
            tree.delete(i)
        cur.execute('select * from emp')
        r=cur.fetchall()
        total=len(r)
        labl.configure(text=total)
        for i in r:
            tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
def sub(*event):
    f=fn.get()
    l=ln.get()
    d=dob.get()
    p=ph.get()
    e=em.get()
    q=qu.get()
    g=ge.get()
    ex=exp.get()
    f1=fa.get()
    m=mo.get()
    a=ad.get()
    i=str(l_code())
    if p!='' and f!='':
        if len(p)==10:
            try:
                int(p)
                sql1 = "INSERT INTO emp (emp_id,first_name,last_name,D_O_B,phone_no,email,qualification,gender,experience,fathers_name,mothers_name,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(i,f,l,d,p,e,q,g,ex,f1,m,a)
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
                e11.delete(0,END)
                messagebox.showinfo('SUCCESS','Successfully registered employee')
            except:
                messagebox.showinfo('ALERT','enter correct phone number')
        else:
            messagebox.showinfo('ALERT','enter correct phone number')                  
    else:
        messagebox.showinfo('ALERT','phone number field or first name should not be empty')
def back6():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        r3.destroy()
        emp_page()    
def emp_reg():
    try:
        r4.destroy()
    except:
        pass
    global fn,ln,dob,ph,em,qu,ge,exp,fa,mo,ad,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,r3
    r3=Tk()
    r3.title('EMPLOYEE REGISTRATION')
    r3.geometry('1200x650')
    r3.resizable(0,0)
    fn=StringVar()
    ln=StringVar()
    dob=StringVar()
    ph=StringVar()
    em=StringVar()
    qu=StringVar()
    ge=StringVar()
    exp=StringVar()
    fa=StringVar()
    mo=StringVar()
    ad=StringVar()
    load = Image.open("images\\w341.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(r3, image=render)
    img.image = render
    img.place(x=-350,y=-130)
    photo1 = PhotoImage(file = "images\\emreg.png")
    Label(r3,image=photo1,bg='#CFD9DA').place(x=10,y=10)
    Label(r3,text='First Name',font=('arial',13),bg='#CFD9DA').place(x=20,y=150)
    e1=Entry(r3,textvariable=fn,font=('arial',13),bd=3,width=30)
    e1.place(x=120,y=150)
    Label(r3,text='Last Name',font=('arial',13),bg='#CFD9DA').place(x=20,y=210)
    e2=Entry(r3,textvariable=ln,font=('arial',13),bd=3,width=30)
    e2.place(x=120,y=210)
    Label(r3,text='D.O.B\n(dd/mm/yyyy)',font=('arial',13),bg='#CFD9DA').place(x=0,y=270)
    e3=Entry(r3,textvariable=dob,font=('arial',13),bd=3,width=30)
    e3.place(x=120,y=270)
    Label(r3,text='Phone Number',font=('arial',13),bg='#CFD9DA').place(x=0,y=330)
    e4=Entry(r3,textvariable=ph,font=('arial',13),bd=3,width=30)
    e4.place(x=120,y=330)
    Label(r3,text='Email',font=('arial',13),bg='#CFD9DA').place(x=20,y=390)
    e5=Entry(r3,textvariable=em,font=('arial',13),bd=3,width=30)
    e5.place(x=120,y=390)
    Label(r3,text='Qualification',font=('arial',13),bg='#CFD9DA').place(x=410,y=150)
    e6=Entry(r3,textvariable=qu,font=('arial',13),bd=3,width=30)
    e6.place(x=530,y=150)
    Label(r3,text='Gender',font=('arial',13),bg='#CFD9DA').place(x=410,y=210)
    e7=ttk.Combobox(r3,values=['Male','Female'],textvariable=ge,width=23,font=('arial',14))
    e7.place(x=530,y=210)
    Label(r3,text='Experience',font=('arial',13),bg='#CFD9DA').place(x=410,y=270)
    e8=Entry(r3,textvariable=exp,font=('arial',13),bd=3,width=30)
    e8.place(x=530,y=270)
    Label(r3,text='Father\'s Name',font=('arial',13),bg='#CFD9DA').place(x=410,y=330)
    e9=Entry(r3,textvariable=fa,font=('arial',13),bd=3,width=30)
    e9.place(x=530,y=330)
    Label(r3,text='Mother\'s Name',font=('arial',13),bg='#CFD9DA').place(x=410,y=390)
    e10=Entry(r3,textvariable=mo,font=('arial',13),bd=3,width=30)
    e10.place(x=530,y=390)
    Label(r3,text='Address',font=('arial',13),bg='#CFD9DA').place(x=200,y=470)
    e11=Entry(r3,textvariable=ad,font=('arial',13),bd=3,width=40)
    e11.place(x=270,y=470)
    photo = PhotoImage(file = "images\\submit.png")
    butt=Button(r3,image=photo,bd=0,activebackground='#CFD9DA',bg='#CFD9DA',command=sub)
    butt.place(x=350,y=505)
    photo55 = PhotoImage(file = "images\\back.png")
    butt=Button(r3,image=photo55,bd=0,activebackground='#CFD9DA',bg='#CFD9DA',command=back6)
    butt.place(x=370,y=570)
    r3.mainloop()
def back10():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        root.destroy()
        man_acc()
def emp_pw_reset():
        global root
        try:
            r7.destroy()
        except:
            pass
        root=Tk()
        root.title('PASSWORD RESET PAGE')
        root.geometry('1100x650')
        load = Image.open("images\\w433.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=-20,y=-170)
        root.resizable(0, 0) 
        e1=StringVar()
        e2=StringVar()
        e3=StringVar()
        e4=StringVar()
        def check():
            i=e1.get()
            s='select password from login_info where username="{}"'.format(str(i))
            cur.execute(s)
            r=cur.fetchone()
            if r==[]:
                messagebox.showinfo('Alert','User Name Not Found')
                return False,None
            else:
                i1=e2.get()
                if i1==r[0]:
                    return True,i
                else:
                    messagebox.showinfo('Alert','Password Do not match with username')
                    return False,None
        def change():
            r,us=check()
            if r:
                n1=e3.get() 
                n2=e4.get()
                if len(n1)>=8:
                    if n1==n2:
                        s='update login_info set password= "{}" where username= "{}"'.format(str(n1),str(us))
                        cur.execute(s)
                        mycon.commit()
                        messagebox.showinfo('ALERT','Successfully updated the password')
                    else:
                        messagebox.showinfo('ALERT','New Password Do not Match with confirm password')
                else:
                    messagebox.showinfo('ALERT','New password entered should be more than 7 characters')
        photo1 = PhotoImage(file = "images\\pwreset.png")
        usr=Label(root,image=photo1,bg='#FFE562')
        usr.place(x=30,y=10)
        Label(root,text='Employee Id',font=('arial',15),bg='#FFE562').place(x=150,y=275)
        id1=Entry(root,textvariable=e1,font=('arial',13),bd=3,width=28 )
        id1.place(x=300,y=275)    
        Label(root,text='Old Password',font=('arial',15),bg='#FFE562').place(x=150,y=320)
        opw=Entry(root,textvariable=e2,show='*',font=('arial',13),bd=3,width=28)
        opw.place(x=300,y=320)    
        Label(root,text='New password',font=('arial',15),bg='#FFE562').place(x=150,y=365)
        npw=Entry(root,textvariable=e3,show='*',font=('arial',13),bd=3,width=28)
        npw.place(x=300,y=365)    
        Label(root,text='Confirm \nNew password',font=('arial',15),bg='#FFE562').place(x=150,y=410)
        cnp=Entry(root,textvariable=e4,show='*',font=('arial',13),bd=3,width=28)
        cnp.place(x=300,y=410)
        def b(*event):
            opw.focus()
        def c(*event):
            npw.focus()
        def d(*event):
            cnp.focus()
        def d(*event):
            cnp.focus()
        photo = PhotoImage(file = "images\\submit.png")
        butt=Button(root,image=photo,bd=0,activebackground='#FFE562',bg='#FFE562',command=change)
        butt.place(x=250,y=500)
        photo3 = PhotoImage(file = "images\\back.png")
        butt1=Button(root,image=photo3,bd=0,activebackground='#FFE562',bg='#FFE562',command=back10)
        butt1.place(x=270,y=570)   
        id1.bind('<Return>',b)
        opw.bind('<Return>',c)
        npw.bind('<Return>',d)        
        cnp.mainloop()       
def back11():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        r3.destroy()
        ViewForm()
def sub1(p):
    s='delete from emp where emp_id ="{}"'.format(p)
    cur.execute(s)
    mycon.commit()
    sub()
    
def emp_up(f):
    global r3
    try:
        viewform.destroy()
    except:
        pass
    global fn,ln,dob,ph,em,qu,ge,exp,fa,mo,ad
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    r3=Tk()
    r3.title('EMPLOYEE UPDATION')
    r3.geometry('1200x650')
    r3.resizable(0,0)
    fn=StringVar()
    ln=StringVar()
    dob=StringVar()
    ph=StringVar()
    em=StringVar()
    qu=StringVar()
    ge=StringVar()
    exp=StringVar()
    fa=StringVar()
    mo=StringVar()
    ad=StringVar()
    load = Image.open("images\\w341.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(r3, image=render)
    img.image = render
    img.place(x=-380,y=-130)
    photo1234 = PhotoImage(file = "images\\emup.png")
    Label(r3,image=photo1234,bg='#CFD9DA').place(x=40,y=10)
    Label(r3,text='First Name',font=('arial',13),bg='#CFD9DA').place(x=20,y=150)
    e1=Entry(r3,textvariable=fn,font=('arial',13),bd=3,width=30)
    e1.place(x=120,y=150)
    Label(r3,text='Last Name',font=('arial',13),bg='#CFD9DA').place(x=20,y=210)
    e2=Entry(r3,textvariable=ln,font=('arial',13),bd=3,width=30)
    e2.place(x=120,y=210)
    Label(r3,text='D.O.B\n(dd/mm/yyyy)',font=('arial',13),bg='#CFD9DA').place(x=0,y=270)
    e3=Entry(r3,textvariable=dob,font=('arial',13),bd=3,width=30)
    e3.place(x=120,y=270)
    Label(r3,text='Phone Number',font=('arial',13),bg='#CFD9DA').place(x=0,y=330)
    e4=Entry(r3,textvariable=ph,font=('arial',13),bd=3,width=30)
    e4.place(x=120,y=330)
    Label(r3,text='Email',font=('arial',13),bg='#CFD9DA').place(x=20,y=390)
    e5=Entry(r3,textvariable=em,font=('arial',13),bd=3,width=30)
    e5.place(x=120,y=390)
    Label(r3,text='Qualification',font=('arial',13),bg='#CFD9DA').place(x=410,y=150)
    e6=Entry(r3,textvariable=qu,font=('arial',13),bd=3,width=30)
    e6.place(x=530,y=150)
    Label(r3,text='Gender',font=('arial',13),bg='#CFD9DA').place(x=410,y=210)
    e7=Entry(r3,textvariable=ge,font=('arial',13),bd=3,width=30)
    e7.place(x=530,y=210)
    Label(r3,text='Experience',font=('arial',13),bg='#CFD9DA').place(x=410,y=270)
    e8=Entry(r3,textvariable=exp,font=('arial',13),bd=3,width=30)
    e8.place(x=530,y=270)
    Label(r3,text='Father\'s Name',font=('arial',13),bg='#CFD9DA').place(x=410,y=330)
    e9=Entry(r3,textvariable=fa,font=('arial',13),bd=3,width=30)
    e9.place(x=530,y=330)
    Label(r3,text='Mother\'s Name',font=('arial',13),bg='#CFD9DA').place(x=410,y=390)
    e10=Entry(r3,textvariable=mo,font=('arial',13),bd=3,width=30)
    e10.place(x=530,y=390)
    Label(r3,text='Address',font=('arial',13),bg='#CFD9DA').place(x=200,y=470)
    e11=Entry(r3,textvariable=ad,font=('arial',13),bd=3,width=40)
    e11.place(x=270,y=470)
    photo = PhotoImage(file = "images\\update.png")
    butt=Button(r3,image=photo,bd=0,activebackground='#CFD9DA',bg='#CFD9DA',command= lambda: sub1(f[0]))
    butt.place(x=350,y=520)
    photo1 = PhotoImage(file = "images\\back.png")
    butt=Button(r3,image=photo1,bd=0,activebackground='#CFD9DA',bg='#CFD9DA',command=back11)
    butt.place(x=360,y=580)
    e1.insert(0,f[1])
    e2.insert(0,f[2])
    e3.insert(0,f[3])
    e4.insert(0,f[4])
    e5.insert(0,f[5])
    e6.insert(0,f[6])
    e7.insert(0,f[7])
    e8.insert(0,f[8])
    e9.insert(0,f[9])
    e10.insert(0,f[10])
    e11.insert(0,f[11])
    r3.mainloop()
def mod():
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        emp_up(f)
    else:
        messagebox.showinfo('ALERT','No record selected for Updation')
def back7():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        viewform.destroy()
        emp_page()
def ViewForm():
    try:
        r4.destroy()
    except:
        pass
    global tree,labl,s1,search2,viewform
    
    cur.execute('select * from emp')
    r=cur.fetchall()
    viewform=Tk()
    viewform.title('VIEW EMPLOYEE')
    viewform.geometry('1200x650')
    s1=StringVar()
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=300)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    text = Label(TopViewForm, text="View Employee Details", font=('arial', 18), width=600)
    text.pack(fill=X)
    txtsearch = Label(LeftViewForm, text="SEARCH \n Enter First Name", font=('arial', 20)).place(x=30,y=25)
    search2 = Entry(LeftViewForm, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "images\\search.png")
    search = Button(LeftViewForm,image=photo,bd=0,command=search1).place(x=70,y=150)
    photo1 = PhotoImage(file = "images\\modify.png")
    reset = Button(LeftViewForm,image=photo1,bd=0,command=mod).place(x=70,y=230)
    photo3 = PhotoImage(file = "images\\delete.png")
    delete = Button(LeftViewForm,image=photo3,bd=0,command=delete_info).place(x=70,y=310)
    photo4 = PhotoImage(file = "images\\reset.png")
    delete = Button(LeftViewForm,image=photo4,bd=0,command=re).place(x=60,y=390)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=('1','2','3','4','5','6','7','8','9','10','11','12'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4','5','6','7','8','9','10','11','12')
    tree['show']='headings'
    tree.heading('1', text="Employee Id")
    tree.heading('2', text="First Name")
    tree.heading('3', text="Last Name")
    tree.heading('4', text="Date Of Birth")
    tree.heading('5', text="Phone number")
    tree.heading('6', text="Email")
    tree.heading('7', text="Qualification")
    tree.heading('8', text="Gender")
    tree.heading('9', text="Experience")
    tree.heading('10', text="Father's Name")
    tree.heading('11', text="Mother's Name")
    tree.heading('12', text="Address")
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
    tree.column('11',width=280,anchor='center')
    tree.column('12',width=280,anchor='center')
    tree.pack()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))
    total=len(r)
    photo44 = PhotoImage(file = "images\\back.png")
    search = Button(LeftViewForm,image=photo44,bd=0,command=back7).place(x=80,y=460)
    Label(viewform,text='TOTAL RESULTS FOUND : ',font=('arial',14)).place(x=40,y=575)
    labl=Label(viewform,text=total,font=('arial',25))
    labl.place(x=140,y=600)
    viewform.mainloop()
def back9():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        root.destroy()
        man_acc()
def acc_create():
        global root
        try:
            r7.destroy()
        except:
                pass
        root=Tk()
        root.title('REGISTRATION PAGE')
        root.geometry('1100x650')
        load = Image.open("images\\w433.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.place(x=-20,y=-170)
        root.resizable(0, 0) 
        e1=StringVar()
        e3=StringVar()
        e4=StringVar()
        def check():
            i=e1.get()
            s='select emp_id from emp where emp_id="{}"'.format(str(i))
            cur.execute(s)
            r=cur.fetchone()
            if r==[]:
                messagebox.showinfo('Alert','Employee Id Not Found')
                return False,None
            else:
                return True,i
        def change():
            r,us=check()
            if r:
                n1=e3.get() 
                n2=e4.get()
                if len(n1)>=8:
                    if n1==n2:
                        
                        s='insert into login_info(l_type,username,password) values("employee",%s,%s)'
                        val=(us,n1)
                        cur.execute(s,val)
                        mycon.commit()
                        messagebox.showinfo('ALERT','Successfully created account')
                    else:
                        messagebox.showinfo('ALERT','New Password Do not Match with confirm password')
                else:
                    messagebox.showinfo('ALERT','New password entered should be more than 7 characters')
        photo2 = PhotoImage(file = "images\\CRE.png")
        usr=Label(root,image=photo2,bg='#FFE562')
        usr.place(x=30,y=10)
        Label(root,text='Employee Id',font=('arial',15),bg='#FFE562').place(x=150,y=275)
        id1=Entry(root,textvariable=e1,font=('arial',13),bd=3,width=28 )
        id1.place(x=300,y=275)      
        Label(root,text='Password',font=('arial',15),bg='#FFE562').place(x=160,y=320)
        npw=Entry(root,textvariable=e3,show='*',font=('arial',13),bd=3,width=28)
        npw.place(x=300,y=320)    
        Label(root,text='Confirm \n Password',font=('arial',15),bg='#FFE562').place(x=160,y=365)
        cnp=Entry(root,textvariable=e4,show='*',font=('arial',13),bd=3,width=28)
        cnp.place(x=300,y=370)
        def b(*event):
            npw.focus()
        def d(*event):
            cnp.focus()
        photo = PhotoImage(file = "images\\submit.png")
        butt1=Button(root,image=photo,bd=0,activebackground='#FFE562',bg='#FFE562',command=change)
        butt1.place(x=230,y=450) 
        photo1 = PhotoImage(file = "images\\back.png")
        butt=Button(root,image=photo1,bd=0,activebackground='#FFE562',bg='#FFE562',command=back9)
        butt.place(x=250,y=550)   
        id1.bind('<Return>',b)
        npw.bind('<Return>',d)        
        root.mainloop()  
def back8():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        r7.destroy()
        emp_page()
def man_acc():
    global r7
    try:
        r4.destroy()
    except:
        pass
    r7=Tk()
    r7.title('EMPLOYEE ACCOUNT MANAGEMENT')
    r7.geometry('1200x650')
    load = Image.open("images\\emppage.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(r7, image=render)
    img.image = render
    img.place(x=0,y=-100)
    photo = PhotoImage(file = "images\\accman.png")
    Label(r7,image=photo,bg='#D6D7D2').place(x=100,y=50)
    photo2 = PhotoImage(file = "images\\createacc.png")
    Button(r7,image=photo2,bg='#D4D3D1',bd=0,activebackground='#D4D3D1',command=acc_create).place(x=110,y=280)
    photo3 = PhotoImage(file = "images\\resetpass.png")
    Button(r7,image=photo3,bg='#D4D3D1',bd=0,activebackground='#D4D3D1',command=emp_pw_reset).place(x=110,y=380)
    photo4 = PhotoImage(file = "images\\back.png")
    Button(r7,image=photo4,bg='#D4D3D1',bd=0,activebackground='#D4D3D1',command=back8).place(x=240,y=470)
    r7.mainloop()
def emp_page():
    global r4
    r4=Tk()
    r4.title('EMPLOYEE DETAILS')
    r4.geometry('1200x650')
    load = Image.open("images\\emppage.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(r4, image=render)
    img.image = render
    img.place(x=0,y=-100)
    photo = PhotoImage(file = "images\\empdet.png")
    Label(r4,image=photo,bg='#D6D7D2').place(x=100,y=50) 
    photo1 = PhotoImage(file = "images\\addemp.png")
    Button(r4,image=photo1,bg='#CFD9DA',bd=0,activebackground='#CFD9DA',command=emp_reg).place(x=140,y=180)
    photo2 = PhotoImage(file = "images\\editemp.png")
    Button(r4,image=photo2,bg='#D4D3D1',bd=0,activebackground='#D4D3D1',command=ViewForm).place(x=140,y=280)
    photo3 = PhotoImage(file = "images\\manageaccount.png")
    Button(r4,image=photo3,bg='#D4D3D1',bd=0,activebackground='#D4D3D1',command=man_acc).place(x=110,y=380)
    r4.mainloop()
emp_page()
