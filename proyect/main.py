#importing modules

import tkinter
from tkinter import *
from tkinter import  ttk
from tkinter import font
from tkinter import messagebox
import mysql.connector

global flagSaleShowBtn, flagProdShowBtn
flagSaleShowBtn = FALSE
flagProdShowBtn = FALSE

db=mysql.connector.connect(
    user="root",
    passwd="root",
    host="localhost"


)
my_cursor=db.cursor() #getting the cursor object
my_cursor.execute("CREATE DATABASE IF NOT EXISTS Shop") #creating the database named library
db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
my_cursor=db.cursor()

#query to create a table products
query="CREATE TABLE IF NOT EXISTS products (date VARCHAR(10),prodName VARCHAR(20), prodPrice VARCHAR(50))" 
my_cursor.execute(query) #executing the query
db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
my_cursor=db.cursor()
#query to create a table sale
query="CREATE TABLE IF NOT EXISTS sale (custName VARCHAR(20), date VARCHAR(10), prodName VARCHAR(30),qty INTEGER, price INTEGER )" 
my_cursor.execute(query) #executing the query


#Create the functions of the program

def prodtoTable():

    pname = prodName.get()
    price = prodPrice.get()
    dt = date.get()
    #connect to database
    db = mysql.connector.connect(user = 'root', passwd='root',host="localhost", database='Shop')
    cursor = db.cursor()

    query = "INSERT INTO products(date, prodName, prodPrice) VALUES(%s, %s, %s)"
    details = (dt, pname, price)

    #executing the query and showing the opo up message
    try:
        cursor.execute(query, details)
        db.commit()
        messagebox.showinfo('Sucess', "prudct added suscess")
    except Exception as e:
        print("the exeption is :", e)
        messagebox.showinfo("Error", "Trouble adding something")
    
   

#function to get details of the product to be added
def addProd():
    global prodName, prodPrice, date, Canvas1, wn

    #Creating the window
    wn = tkinter.Tk()    
    wn.title("Python Geeks shop")
    wn.configure(bg= 'mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg= 'LightBlue1')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="add a product", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=0.8, relheight=0.4)


    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)


    #GettingDate
    lable1= Label(labelFrame, text="Date : ", fg='black')
    lable1.place(relx=0.05, rely=0.3, relheight=0.08)

    date = Entry(labelFrame)
    date.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    lable2= Label(labelFrame, text="Product Name : ", fg='black')
    lable2.place(relx=0.05, rely=0.45, relheight=0.08)

    prodName = Entry(labelFrame)
    prodName.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.08)

    lable3= Label(labelFrame, text="Product Price : ", fg='black')
    lable3.place(relx=0.05, rely=0.6, relheight=0.08)

    prodPrice = Entry(labelFrame)
    prodPrice.place(relx=0.3, rely=0.6, relwidth=0.62, relheight=0.08)

    Btn = Button(wn, text="ADD", bg='green', fg='black', command=prodtoTable)
    Btn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

    Quit= Button(wn,text="Quit",bg='#f7f1e3', fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()


def delProd():

    global wn, prodName

    wn = tkinter.Tk()
    wn.title("Python Geeks shop")
    wn.configure(bg= 'mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg= 'LightBlue1')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete a Product", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=0.8, relheight=0.4)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #Getting the product
    lable1= Label(labelFrame, text="Product Name : ", fg='black')
    lable1.place(relx=0.05, rely=0.45, relheight=0.08)

    prodName = Entry(labelFrame)
    prodName.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.08)

    #Create a delete button
    Delbtn = Button(wn, text= "Delete", bg='red', fg='black', command=delProdAction)
    Delbtn.place(relx=0.1, rely=0.85, relwidth=.18, relheight=.1)

    #Create a quit button
    Quitbtn = Button(wn,text="Quit", bg='green', fg='black', command=wn.destroy )
    Quitbtn.place(relx=0.56, rely=0.85, relwidth=.18, relheight=.1)
    wn.mainloop()

def delProdAction():
    
    db = mysql.connector.connect(host = "localhost", user="root", password = "root", database="shop" )
    cursor  =  db.cursor()    
    query = "Delete from products WHERE prodName = '"+prodName.get()+"'"   
    try:
        cursor.execute(query)
        db.commit()
        messagebox.showinfo('Sucess', "prudct deleted suscess")
    except Exception as e:
        print("the exeption is :", e)
        messagebox.showinfo("Error", "Trouble deleted something")

      


    



def viewSales():

    
    global wn, flagSaleShowBtn, flagProdShowBtn

    wn = tkinter.Tk()
    wn.title("Python Geeks shop")
    wn.configure(bg= 'mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg= 'LightBlue1')
    Canvas1.pack(expand=True, fill=BOTH)
    headingLabeltext = "" 
    label1text = ""
    label2text = ""
    label3text = ""
    querytext = ""

    
   
    headingLabeltext = "View all Sales" 
    label1text = "Costumer"
    label2text = "Date"
    label3text = "Product"
    label3text = "Quantity"
    querytext = "SELECT * FROM sale"

    

        

    headingFrame1 = Frame( wn, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0, rely=0.05, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text= headingLabeltext, fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0.3,rely=0, relwidth=0.8, relheight=0.4)


    labelFrame = Frame( wn)
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.9)


    db = mysql.connector.connect(user = 'root', passwd='root',host="localhost", database='shop')
    query = db.cursor()
    
    listbox = Listbox(labelFrame, height = 10, width = 15, bg = 'grey', activestyle= 'dotbox', font = 'Helvetica"', fg = "yellow")

    label1 = Label(labelFrame, text = label1text)
    label1.place(relx=0.00, rely=0.0, relwidth=0.05, relheight=0.05)
    label2 = Label(labelFrame, text = label2text)
    label2.place(relx=0.2, rely=0.0, relwidth=0.05, relheight=0.05)
    label3 = Label(labelFrame, text = label3text)
    label3.place(relx=0.4, rely=0.0, relwidth=0.05, relheight=0.05)
    
    


    try:
         query.execute(querytext)
         #messagebox.showinfo('Success', "Suceess to show products")
         listboxcount = 0
         for x in query:
                listboxcount= listboxcount+1 
                listbox.insert(listboxcount,x)       
    except Exception as e :
           print("this execption is : ", e)
           messagebox.showinfo('Error ', "Error in something with the Databases")
   
    listbox.place(relx=0.0, rely=0.1, relwidth=1, relheight=1)       

   

    Quitbtn = Button(wn, text="Quit", bg='yellow', fg='black', command=wn.destroy)
    Quitbtn.place(relx=0.8, rely=0.8, relwidth=.18, relheight=.1)
    
    
    wn.mainloop()
   

def viewProds():

    
    global wn, flagSaleShowBtn, flagProdShowBtn

    wn = tkinter.Tk()
    wn.title("Python Geeks shop")
    wn.configure(bg= 'mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg= 'LightBlue1')
    Canvas1.pack(expand=True, fill=BOTH)
    headingLabeltext = "" 
    label1text = ""
    label2text = ""
    label3text = ""
    querytext = ""

    
    headingLabeltext = "View all Products" 
    label1text = "Date"
    label2text = "Item"
    label3text = "Cost"
    querytext = "SELECT * FROM products"
    

 

        

    headingFrame1 = Frame( wn, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0, rely=0.05, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text= headingLabeltext, fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0.3,rely=0, relwidth=0.8, relheight=0.4)


    labelFrame = Frame( wn)
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.9)


    db = mysql.connector.connect(user = 'root', passwd='root',host="localhost", database='shop')
    query = db.cursor()
    
    listbox = Listbox(labelFrame, height = 10, width = 15, bg = 'grey', activestyle= 'dotbox', font = 'Helvetica"', fg = "yellow")

    label1 = Label(labelFrame, text = label1text)
    label1.place(relx=0.00, rely=0.0, relwidth=0.05, relheight=0.05)
    label2 = Label(labelFrame, text = label2text)
    label2.place(relx=0.2, rely=0.0, relwidth=0.05, relheight=0.05)
    label3 = Label(labelFrame, text = label3text)
    label3.place(relx=0.4, rely=0.0, relwidth=0.05, relheight=0.05)
    
    


    try:
         query.execute(querytext)
         #messagebox.showinfo('Success', "Suceess to show products")
         listboxcount = 0
         for x in query:
            listboxcount= listboxcount+1 
            listbox.insert(listboxcount,x)       
    except Exception as e :
           print("this execption is : ", e)
           messagebox.showinfo('Error ', "Error in something with the Databases")
   
    listbox.place(relx=0.0, rely=0.1, relwidth=1, relheight=1)       

    
    Quitbtn = Button(wn, text="Quit", bg='yellow', fg='black', command=wn.destroy)
    Quitbtn.place(relx=0.5, rely=0.8, relwidth=.18, relheight=.1)
    
    
    wn.mainloop()
    
    
def newCust():
    pass

def saltoTable():
    #custName
    #date
    #prodName
    #qty
    #price
    
    custname = custName.get()
    dt = date.get()
    prodname = prodName.get()
    qt = int(qty.get())   
    
    #connect to database
    db = mysql.connector.connect(user = 'root', passwd='root',host="localhost", database='shop')
    cursor = db.cursor()

    query = "INSERT INTO sale(custName, date, prodName, qty) VALUES(%s, %s, %s, %s)"
    details = (custname, dt, prodname,qt)

    #executing the query and showing the opo up message
    try:
        cursor.execute(query, details)
        db.commit()
        messagebox.showinfo('Sucess', "Sale  added suscess")
    except Exception as e:
        print("the exeption is :", e)
        messagebox.showinfo("Error", "Trouble adding something")

def salProd():
    
    global custName, prodName, prodPrice, date, Canvas1, wn, qty
    



    #Creating the window
    wn = tkinter.Tk()    
    wn.title("Sale  a Product")
    wn.configure(bg= 'mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg= 'LightBlue1')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg="LightBlue1", bd=5)
    headingFrame1.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Sale of a Product", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=0.8, relheight=0.4)


    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)


    #GettingDate
    lable1= Label(labelFrame, text="Customer Name : ", fg='black')
    lable1.place(relx=0.05, rely=0.3, relheight=0.08)

    custName = Entry(labelFrame)
    custName.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    lable2= Label(labelFrame, text="Date : ", fg='black')
    lable2.place(relx=0.05, rely=0.45, relheight=0.08)

    date = Entry(labelFrame)
    date.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.08)

    lable3= Label(labelFrame, text="Product Name : ", fg='black')
    lable3.place(relx=0.05, rely=0.6, relheight=0.08)

    prodName = Entry(labelFrame)
    prodName.place(relx=0.3, rely=0.6, relwidth=0.62, relheight=0.08)

    lable4= Label(labelFrame, text="Cuantity : ", fg='black')
    lable4.place(relx=0.05, rely=0.75, relheight=0.08)

    qty = Entry(labelFrame)
    qty.place(relx=0.3, rely=0.75, relwidth=0.62, relheight=0.08)

    Btn = Button(wn, text="ADD", bg='green', fg='black', command=saltoTable)
    Btn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

    Quit= Button(wn,text="Quit",bg='#f7f1e3', fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()
  
    




   


#creating the main window
wn = tkinter.Tk()
wn.title("Proyect 1 ")
wn.configure(bg='honeydew2')
wn.minsize(width=500, height=500)
wn.geometry("700x600")

headingFrame1 = Frame(wn, bg= "snow3", bd=5)
headingFrame1.place(relx=0.2, rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to my shop \n Bienvenido a mi tienda", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#Button to add a new product
btn1 = Button(wn,text="Add a Product",bg='LightBlue1', fg='black', width=20,height=2, command=addProd)
btn1['font'] = font.Font( size=12)
btn1.place(x=270,y=175)

#Button to delete a product
btn2 = Button(wn,text="Delete a Product",bg='misty rose', fg='black',width=20,height=2,command=delProd)
btn2['font'] = font.Font( size=12)
btn2.place(x=270,y=255)

#Button to view all products
btn3 = Button(wn,text="View Products",bg='old lace', fg='black',width=20,height=2,command=viewProds)
btn3['font'] = font.Font( size=12)
btn3.place(x=270,y=335)

#Button to view all products
btn6 = Button(wn,text="View Sales",bg='old lace', fg='black',width=20,height=2,command=viewSales)
btn6['font'] = font.Font( size=12)
btn6.place(x=270,y=415)

#Button to add a new sale and generate bill
btn4 = Button(wn,text="Sale",bg='lavender blush2', fg='black', width=20,height=2,command = salProd)
btn4['font'] = font.Font( size=12)
btn4.place(x=270,y=490)

#Button to exit
btn5 = Button(wn,text="EXIT",bg='lavender blush2', fg='black', width=20,height=2,command = wn.destroy)
btn5['font'] = font.Font( size=12)
btn5.place(x=270,y=550)


wn.mainloop() 