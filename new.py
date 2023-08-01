from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("C:\\Users\\dorai\\OneDrive\\Desktop\\grocery.db")

root = Tk()

root.title("Grocery.com")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.resizable(False, False)
imgTemp = Image.open("shop.jpg")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)
label = Label(root,image=img)
label.pack(side='top',fill=Y,expand=True)

def add():
    summation=int(150*int(e1.get()))+(100*int(e2.get()))+(120*int(e3.get()))+(160*int(e4.get()))+(80*int(e5.get()))+(80*int(e6.get()))+(70*int(e7.get()))+(120*int(e8.get()))+(80*int(e9.get()))+(80*int(e10.get()))
    total=int(summation)
    label1 = Label(root,text="Amount is: "+str(total),font=('arial',22)).place(x=1100,y=350)
    
def place_order():
    try:
        cursor=conn.cursor()
        name=e.get()
        mobile=int(mobile1.get())
        address=e0.get()
        apple=e1.get()
        orange=e2.get()
        guava=e3.get()
        mango=e4.get()
        papaya=e5.get()
        dragon=e6.get()
        mausambi=e7.get()
        berries=e8.get()
        grapes=e9.get()
        jamun=e10.get()
        summation=int(150*int(e1.get()))+(100*int(e2.get()))+(120*int(e3.get()))+(160*int(e4.get()))+(80*int(e5.get()))+(80*int(e6.get()))+(70*int(e7.get()))+(120*int(e8.get()))+(80*int(e9.get()))+(80*int(e10.get()))
        total=int(summation)
        label1 = Label(root,text="Total bill is :"+str(total),font=('arial',22)).place(x=600,y=710)
        cursor.execute("Insert into customer (customer_name,mobile_number,customer_address,Total_bill) values(?,?,?,?)", (name,mobile,address,summation))
        cursor.execute("Insert into orders (customer_name,Apple,Orange,Guava,Mango,Papaya,Dragon_fruit,Mausambi,Berries,Grapes,Jamun,Total_bill) values(?,?,?,?,?,?,?,?,?,?,?,?)", (name,apple,orange,guava,mango,papaya,dragon,mausambi,berries,grapes,jamun,summation))
        conn.commit()
        messagebox.showinfo("Status","Please press NEXT button to place your order")
    except:
        messagebox.showinfo("Status","Cannot place the order")

def msg():
    try:
         messagebox.showinfo("Status","Successfully!! Placed your order :)")
    except:
        messagebox.showinfo("Status","Cannot place the order")

def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("Order Details")
    newWindow.geometry("900x900")
    newWindow.configure(bg='light grey')
    Label(newWindow,text ="Order details ",font=('arial',22)).place(x=10,y=20)
    Label(newWindow,text="Total Bill is:- ",font=('times',15),background='white').place(x=100,y=100)

    Label(newWindow,text=e.get(),font=('times',15),background='white').place(x=400,y=100)
    Label(newWindow,text=emob.get(),font=('times',15),background='white').place(x=500,y=100)
    Label(newWindow,text=e0.get(),font=('times',15),background='white').place(x=700,y=100)
    
    Label(newWindow,text="1. Apple",font=('times',12),background='white').place(x=100,y=150)
    apple_price=(150*int(price1.get()))
    Label(newWindow,text=int(apple_price),font=('times',12),background='white').place(x=200,y=150)
    
    Label(newWindow,text="2. Orange",font=('times',12),background='white').place(x=100,y=200)
    orange_price=(100*int(price2.get()))
    Label(newWindow,text=int(orange_price),font=('times',12),background='white').place(x=200,y=200)
    
    Label(newWindow,text="3. Guava",font=('times',12),background='white').place(x=100,y=250)
    guava_price=(120*int(price3.get()))
    Label(newWindow,text=int(guava_price),font=('times',12),background='white').place(x=200,y=250)
    
    Label(newWindow,text="4. Mango",font=('times',12),background='white').place(x=100,y=300) 
    mango_price=(160*int(price4.get()))
    Label(newWindow,text=int(mango_price),font=('times',12),background='white').place(x=200,y=300)
    
    Label(newWindow,text="5. Papaya",font=('times',12),background='white').place(x=100,y=350)
    papaya_price=(80*int(price5.get()))
    Label(newWindow,text=int(papaya_price),font=('times',12),background='white').place(x=200,y=350)
    
    Label(newWindow,text="6. Dragon Fruit",font=('times',12),background='white').place(x=100,y=400)
    dragon_price=(80*int(price6.get()))
    Label(newWindow,text=int(dragon_price),font=('times',12),background='white').place(x=210,y=400)
    
    Label(newWindow,text="7. Mausambi",font=('times',12),background='white').place(x=100,y=450)
    mausambi_price=(70*int(price7.get()))
    Label(newWindow,text=int(mausambi_price),font=('times',12),background='white').place(x=200,y=450)
    
    Label(newWindow,text="8. Berries",font=('times',12),background='white').place(x=100,y=500)
    berries_price=(120*int(price8.get()))
    Label(newWindow,text=int(berries_price),font=('times',12),background='white').place(x=200,y=500)
    
    Label(newWindow,text="9. Grapes",font=('times',12),background='white').place(x=100,y=550)
    grapes_price=(80*int(price9.get()))
    Label(newWindow,text=int(grapes_price),font=('times',12),background='white').place(x=200,y=550)
    
    Label(newWindow,text="10. Jamun",font=('times',12),background='white').place(x=100,y=600)
    jamun_price=(80*int(price10.get()))
    Label(newWindow,text=int(jamun_price),font=('times',12),background='white').place(x=200,y=600)
    
    Label(newWindow,text="Total",font=('times',12),background='white').place(x=100,y=700)
    total=(150*int(price1.get()))+(100*int(price2.get()))+(120*int(price3.get()))+(160*int(price4.get()))+(80*int(price5.get()))+(80*int(price6.get()))+(70*int(price7.get()))+(120*int(price8.get()))+(80*int(price9.get()))+(80*int(price10.get()))
    Label(newWindow,text=int(total),font=('times',12),background='white').place(x=200,y=700)

    btn1 = Button(newWindow,text ="Place Order",bg='light grey',height=2,width=15,fg='Black',command =msg).place(x=400,y=500)

photo=Image.open("logo.jpg")
photo=photo.resize((250,185))
my=ImageTk.PhotoImage(photo)
photo_label=Label(image=my)
photo_label.place(x=10,y=20)

Label(root,text="Open Daily 9am to 10pm",font=('times',18),background='white').place(x=1115,y=30)

Label(root,text="ORDER ITEMS",font=('arial',22),background='white').place(x=300,y=220)

Label(root,text="Quantity(kg)",font=('times',15),background='white').place(x=215,y=300)
Label(root,text="Items",font=('times',15),background='white').place(x=100,y=300)

name=StringVar()
Label(root,text="Name: ",font=('times',18),background='white').place(x=455,y=100)
e=Entry(root,textvariable=name,font=('times',18))
e.place(x=550,y=100)

mobile1=IntVar()
Label(root,text="Mobile: ",font=('times',18),background='white').place(x=850,y=100)
emob=Entry(root,textvariable=mobile1,font=('times',18))
emob.place(x=950,y=100)

address=StringVar()
Label(root,text="Address : ",font=('times',18),background='white').place(x=455,y=150)
e0=Entry(root,textvariable=address,font=('times',18))
e0.place(x=565,y=150)

price1=IntVar()
Label(root,text="1. Apple",font=('times',15),background='white').place(x=100,y=350)
e1=Entry(root,textvariable=price1)
e1.place(x=200,y=355)
b1=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=350,y=350)

price2=IntVar()
Label(root,text="2. Orange",font=('times',15),background='white').place(x=100,y=400)
e2=Entry(root,textvariable=price2)
e2.place(x=200,y=400)
b2=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=350,y=400)

price3=IntVar()
Label(root,text="3. Guava",font=('times',15),background='white').place(x=100,y=450)
e3=Entry(root,textvariable=price3)
e3.place(x=200,y=450)
b3=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=350,y=450)

price4=IntVar()
Label(root,text="4. Mango",font=('times',15),background='white').place(x=100,y=500)
e4=Entry(root,textvariable=price4)
e4.place(x=200,y=500)
b4=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=350,y=500)

price5=IntVar()
Label(root,text="5. Papaya",font=('times',15),background='white').place(x=100,y=550)
e5=Entry(root,textvariable=price5)
e5.place(x=200,y=550)
b5=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=350,y=550)

price6=IntVar()
Label(root,text="6. Dragon fruit",font=('times',15),background='white').place(x=570,y=350)
e6=Entry(root,textvariable=price6)
e6.place(x=720,y=355)
b6=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=855,y=350)

price7=IntVar()
Label(root,text="7. Mausambi",font=('times',15),background='white').place(x=570,y=400)
e7=Entry(root,textvariable=price7)
e7.place(x=720,y=405)
b7=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=855,y=400)

price8=IntVar()
Label(root,text="8. Berries",font=('times',15),background='white').place(x=570,y=450)
e8=Entry(root,textvariable=price8)
e8.place(x=720,y=455)
b8=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=855,y=450)

price9=IntVar()
Label(root,text="9. Grapes",font=('times',15),background='white').place(x=570,y=500)
e9=Entry(root,textvariable=price9)
e9.place(x=720,y=505)
b9=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=855,y=500)

price10=IntVar()
Label(root,text="10. Jamun",font=('times',15),background='white').place(x=570,y=550)
e10=Entry(root,textvariable=price10)
e10.place(x=720,y=555)
b10=Button(root,text="Add",bg='light grey',height=1,width=15,fg='Black',command=add).place(x=855,y=550)

btn = Button(root,text ="Next",bg='light grey',height=2,width=15,fg='Black',command = openNewWindow).place(x=800,y=650)

but=Button(root,text="order details",bg='light grey',height=2,width=15,fg='Black',command=place_order).place(x=600,y=650)

root.mainloop()


