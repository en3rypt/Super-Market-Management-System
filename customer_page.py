from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from tkinter import ttk
from PIL import Image, ImageTk
mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
cur=mycon.cursor()
def back3():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        root.destroy()
        view_cus()        
def reg1():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        root.destroy()
        cus_page()
def customer_up_and_add(mode,na,ma,p,ad):   
    if mode=='register':
        try:
            root1.destroy()
        except:
            pass   
    global root
    root=Tk()
    a=StringVar()
    a1=StringVar()
    a2=StringVar()
    a3=StringVar()
    def sub(*event):
        t=a.get()
        t1=a1.get()
        t2=a2.get()
        t3=a3.get()
        cur.execute('select phone_no from customer')
        r=cur.fetchall()
        if t2!='' and t!='':
            if len(t2)==10:
                try:
                    int(t2)
                    try:
                        sql1 = "INSERT INTO customer(phone_no,Name,address,email) values(%s,%s,%s,%s)"
                        val=(t2,t,t3,t1)
                        cur.execute(sql1,val)
                        mycon.commit()
                        first_name.delete(0,END)
                        email.delete(0,END)
                        phone.delete(0,END)
                        add.delete(0,END)
                        messagebox.showinfo('ALERT','successfully registered customer')
                    except mysql.connector.errors.IntegrityError:
                        messagebox.showinfo('ALERT','Phone number already exists')
                except:    
                    messagebox.showinfo('ALERT','Enter correct phone number')
            else:
                messagebox.showinfo('ALERT','Enter correct phone number')                  
        else:
            messagebox.showinfo('ALERT','Phone number field or Name should not be empty')
    def b(p):
        t=a.get()
        t1=a1.get()
        t2=a2.get()
        t3=a3.get()
        
        s='delete from customer where phone_no ="{}"'.format(p)
        cur.execute(s)
        mycon.commit()
        sql1 = "INSERT INTO customer(phone_no,Name,address,email) values(%s,%s,%s,%s)"
        val=(t2,t,t1,t3)
        cur.execute(sql1, val)
        mycon.commit()
        first_name.delete(0,END)
        email.delete(0,END)
        phone.delete(0,END)
        add.delete(0,END)
        messagebox.showinfo('ALERT','successfully updated info')
        root.destroy()
        view_cus()
    root.geometry('1200x650')
    load = Image.open("images\\w113.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=0,y=0)
    root.resizable(0, 0)
    Label(root,text='Name',font=('arial',15),bg='#C4E7EB').place(x=385,y=275)
    first_name=Entry(root,textvariable=a,font=('arial',13),bd=3,width=28 )
    first_name.place(x=460,y=275)    
    Label(root,text='Address',font=('arial',15),bg='#C4E7EB').place(x=365,y=320)
    email=Entry(root,textvariable=a1,font=('arial',13),bd=3,width=28)
    email.place(x=460,y=320)    
    Label(root,text='Phone',font=('arial',15),bg='#C4E7EB').place(x=380,y=365)
    phone=Entry(root,textvariable=a2,font=('arial',13),bd=3,width=28)
    phone.place(x=460,y=365)    
    Label(root,text='Email',font=('arial',15),bg='#C4E7EB').place(x=385,y=410)
    add=Entry(root,textvariable=a3,font=('arial',13),bd=3,width=28)
    add.place(x=460,y=410)
    def a22(*event):
        email.focus()
    def b22(*event):
        phone.focus()
    def c22(*event):
        add.focus()
    if mode=='register':
        root.title('REGISTRATION PAGE')
        ln=StringVar()
        em=StringVar()
        ph=StringVar()
        ad=StringVar()
        usr=Label(root,text='CUSTOMER REGISTRATION',font=('TIMES',30,'bold'),bg='#C4E7EB')
        usr.place(x=300,y=180)
        photo = PhotoImage(file = "images\\submit.png")
        butt1=Button(root,image=photo,bd=0,activebackground='#C4E7EB',bg='#C4E7EB',command=sub)
        butt1.place(x=500,y=450)
    elif mode=='update':
        root.title('UPDATION PAGE')
        usr=Label(root,text='UPDATE CUSTOMER',font=('TIMES',30,'bold'),bg='#C4E7EB')
        usr.place(x=350,y=180)
        photo = PhotoImage(file = "images\\update.png")
        butt=Button(root,image=photo,bd=0,activebackground='#C4E7EB',bg='#C4E7EB',command= lambda: b(p))
        butt.place(x=500,y=450)
    
        first_name.insert(0,na)
        email.insert(0,ma)
        phone.insert(0,p)
        add.insert(0,ad)
    
    photo2 = PhotoImage(file = "images\\back.png")
    butt=Button(root,image=photo2,bd=0,activebackground='#C4E7EB',bg='#C4E7EB',command=back3) 
    butt.place(x=520,y=520)
    first_name.bind('<Return>',a22)
    email.bind('<Return>',b22)
    phone.bind('<Return>',c22)
    root.mainloop()
def delete_info1(*event):
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        p1=str(f[0])
        s='delete from customer where phone_no = '+p1
        cur.execute(s)
        mycon.commit()
        for i in tree.get_children():
            tree.delete(i)
        cur.execute('select * from customer')
        r=cur.fetchall()
        total=len(r)
        labl.configure(text=total)
        for i in r:
            tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
        mycon.close()
def search11():
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    p=s1.get()
    if p!='':
        try:
            int(p)
            search2.delete(0,END)
            sql1='select * from customer where phone_no ='+p
            cur.execute(sql1)
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in tree.get_children():
                tree.delete(i)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
            mycon.close()
        except:
            messagebox.showinfo('ALERT!','Enter only phone number.')
def modify1():
        if tree.focus():
            f=tree.item(tree.focus())
            f=f['values'] 
            p,na,ma,ad=f[0],f[1],f[2],f[3]
            viewform.destroy()
            customer_up_and_add('update',na,ma,p,ad)
        else:
            messagebox.showinfo('ALERT','no field is selected')
def re1():
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    cur.execute('select * from customer')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
    mycon.close()
def back2():
    if messagebox.askquestion('ALERT','Do you want to go back?')=='yes':
        viewform.destroy()
        cus_page()        
def view_cus():
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    global labl,s1,search2,tree,viewform
    try:
        root1.destroy()
    except:
        pass
    viewform=Tk()
    viewform.geometry('1200x650')
    viewform.title('VIEW CUSTOMER')
    s1=StringVar()
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=300)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    text = Label(TopViewForm, text="View Customer Details", font=('arial', 18), width=600)
    text.pack(fill=X)
    txtsearch = Label(LeftViewForm, text="SEARCH\n Phone No", font=('arial', 20)).place(x=70,y=30)
    search2 = Entry(LeftViewForm, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "images\\search.png")
    search = Button(LeftViewForm,image=photo,bd=0,command=search11).place(x=70,y=150)
    photo1 = PhotoImage(file = "images\\modify.png")
    reset = Button(LeftViewForm,image=photo1,bd=0,command=modify1).place(x=70,y=230)
    photo3 = PhotoImage(file = "images\\delete.png")
    delete = Button(LeftViewForm,image=photo3,bd=0,command=delete_info1).place(x=70,y=310)
    photo4 = PhotoImage(file = "images\\reset.png")
    delete = Button(LeftViewForm,image=photo4,bd=0,command=re1).place(x=60,y=390)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=('1','2','3','4','5','6','7','8','9','10','11','12'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4')
    tree['show']='headings'
    tree.heading('1',text='phone number')
    tree.heading('2',text='Name')
    tree.heading('3',text='address')
    tree.heading('4',text='mail')
    tree.column('4',width=280,anchor='center')
    tree.column('3',width=240,anchor='center')
    tree.column('2',width=240,anchor='center')
    tree.column('1',width=170,anchor='center')
    tree.pack()
    cur.execute('select * from customer')
    r=cur.fetchall()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
    total=len(r)
    photo44 = PhotoImage(file = "images\\back.png")
    search = Button(LeftViewForm,image=photo44,bd=0,command=back2).place(x=80,y=460)
    Label(viewform,text='TOTAL RESULTS FOUND : ',font=('arial',14)).place(x=40,y=575)
    labl=Label(viewform,text=total,font=('arial',25))
    labl.place(x=140,y=600)
    viewform.mainloop()
def cus_page():
    global root1,mycon,cur
    root1=Tk()
    mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
    cur=mycon.cursor()
    root1.title('CUSTOMER DETAILS')
    root1.geometry('1190x650')
    load = Image.open("images\\w63.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root1, image=render)
    img.image = render
    img.place(x=-10,y=-80)
    photo4 = PhotoImage(file = "images\\addcus.png")
    canvas = Canvas(root1, width=610, height=340,bg='#D8C1B3')
    canvas.place(x=300,y=180)
    Label(root1,text='CUSTOMER DETAILS',bg='#D8C1B3',fg='red',font=('times',40)).place(x=340,y=200) 
    Button(root1,image=photo4,activebackground='#D8C1B3',bd=0,bg='#D8C1B3',command= lambda: customer_up_and_add('register','','','','')).place(x=420,y=300)
    photo5 = PhotoImage(file = "images\\editcus.png")
    Button(root1,image=photo5,activebackground='#D8C1B3',bd=0,bg='#D8C1B3',command=view_cus).place(x=415,y=400)
    root1.mainloop()

