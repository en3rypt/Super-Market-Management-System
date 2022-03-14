from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
def backc():
    root11.destroy()
    main_income_page() 
def total_income_page():
    global root11
    try:
        root9.destroy()
    except:
        pass
    root11=Tk()
    root11.title('ANNUAL INCOMME PAGE')
    def getval():
        mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
        cur=mycon.cursor()
        v2=c2.get()
        s='total_income_{}'.format(v2)
        try:
            sql1='select total_income from {}'.format(s)
            cur.execute(sql1)
            r=cur.fetchone()
            total=r[0]
            l1.configure(text=total)
        except sql.errors.ProgrammingError:
            messagebox.showerror('ALERT','No record found!')
    root11.geometry('1200x650')
    root11.resizable(0,0)
    load = Image.open("images\\win.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root11, image=render)
    img.image = render
    img.place(x=0,y=0)
    photo = PhotoImage(file = "images\\ann.png")
    a1=Label(root11,image=photo,bg='#FECA1E')
    a1.place(x=400,y=20)
    Label(root11,text='SELECT YEAR',bg='#FCC721',font=('arial',15)).place(x=510,y=250)
    c2 = ttk.Combobox(root11,width=20 ,font=('arial',15),values=["2018","2019","2020","2021","2022","2023","2024","2025"])
    c2.place(x=700,y=250)
    photo1=PhotoImage(file='images\\search.png')
    b1=Button(root11,image=photo1,bd=0,command=getval,bg='#FFC708',activebackground='#FFC708')
    b1.place(x=630,y=300)
    photo2=PhotoImage(file='images\\back.png')
    b1=Button(root11,image=photo2,bd=0,command=backc,bg='#FFC708',activebackground='#FFC708')
    b1.place(x=640,y=370)
    Label(root11,text='INCOME: ',bg='#FEC804',font=('TIMES',35,'bold')).place(x=510,y=500)
    l1=Label(root11,text=' ',bg='#FEC804',font=('TIMES',35,'bold'))
    l1.place(x=740,y=500)
    root11.mainloop()

def backb():
    root10.destroy()
    main_income_page()
def month_income_page():
    global root10
    try:
        root9.destroy()
    except:
        pass
    root10=Tk()
    root10.title('MONTHLY INCOME PAGE')
    def getval():
        mycon=sql.connect(host='localhost',user='root',passwd='root',database='supermarket')
        cur=mycon.cursor()
        v1=c1.get()
        v2=c2.get()
        s='income_{}_{}'.format(v1,v2)
        try:
            sql1='select monthly_income from {}'.format(s)
            cur.execute(sql1)
            r=cur.fetchone()
            total=r[0]
            l1.configure(text=total)
        except sql.errors.ProgrammingError:
            messagebox.showerror('ALERT','No record found!')
    root10.geometry('1200x650')
    root10.resizable(0,0)
    load = Image.open("images\\win.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root10, image=render)
    img.image = render
    img.place(x=0,y=0)
    photo = PhotoImage(file = "images\\monthi.png")
    a1=Label(root10,image=photo,bg='#FECA1E')
    a1.place(x=400,y=20)
    Label(root10,text='SELECT MONTH',bg='#FCC721',font=('arial',15)).place(x=510,y=200)
    c1 = ttk.Combobox(root10,width=20 ,font=('arial',15),values=["January","Febuary","March","April","May","June","July","August","September","October","November","December"])
    c1.place(x=700,y=200)
    Label(root10,text='SELECT YEAR',bg='#FCC721',font=('arial',15)).place(x=510,y=250)
    c2 = ttk.Combobox(root10,width=20 ,font=('arial',15),values=["2018","2019","2020","2021","2022","2023","2024","2025"])
    c2.place(x=700,y=250)
    photo1=PhotoImage(file='images\\search.png')
    b1=Button(root10,image=photo1,bd=0,command=getval,bg='#FFC708',activebackground='#FFC708')
    b1.place(x=630,y=300)
    photo2=PhotoImage(file='images\\back.png')
    b1=Button(root10,image=photo2,bd=0,command=backb,bg='#FFC708',activebackground='#FFC708')
    b1.place(x=640,y=370)
    Label(root10,text='INCOME: ',bg='#FEC804',font=('TIMES',35,'bold')).place(x=510,y=500)
    l1=Label(root10,text=' ',bg='#FEC804',font=('TIMES',35,'bold'))
    l1.place(x=740,y=500)
    root10.mainloop()
def backm():
    root9.destroy()
def main_income_page():
    global root9
    root9 = Tk()
    root9.geometry('1200x650')
    root9.title('INCOME PAGE')
    root9.resizable(0,0)
    load = Image.open("images\\win.jpg")
    photo1=PhotoImage(file='images\\monthb.png')
    photo2=PhotoImage(file='images\\annualb.png')
    photo3=PhotoImage(file='images\\back.png')
    photo = PhotoImage(file = "images\\incomp.png")
    render = ImageTk.PhotoImage(load)
    img = Label(root9, image=render)
    img.image = render
    img.place(x=0,y=0)
    a1=Label(root9,image=photo,bg='#FECA1E')
    a1.place(x=450,y=20)
    b1=Button(root9,image=photo1,bd=0,command=month_income_page,bg='#FFC708',activebackground='#FFC708')
    b1.place(x=520,y=240)
    b2=Button(root9,image=photo2,bd=0,bg='#FFC708',command=total_income_page,activebackground='#FFC708')
    b2.place(x=520,y=380)
    b3=Button(root9,image=photo3,bd=0,bg='#FFC708',command= lambda: root9.destroy(),activebackground='#FFC708')
    b3.place(x=680,y=480)
    root9.mainloop()
   

