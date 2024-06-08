from tkinter import *
from tkinter import messagebox as msg
root=Tk()
root.title("Calculator")
root.geometry('1000x1000')
root.resizable(False,False)

def add():
    if name_entry1.get()=="" or name_entry2.get()=="":
        msg.showinfo("Alert !!!","The Data Should Not Be Empty")
    else:
        n1=int(name_entry1.get())
        n2=int(name_entry2.get())
        msg.showinfo("Addition",f"{n1+n2}")
def sub():
    if name_entry1.get()=="" or name_entry2.get()=="":
        msg.showinfo("Alert !!!","The Data Should Not Be Empty")
    else:
        n1=int(name_entry1.get())
        n2=int(name_entry2.get())
        msg.showinfo("Subraction",f"{n1-n2}")
def mul():
    if name_entry1.get()=="" or name_entry2.get()=="":
        msg.showinfo("Alert !!!","The Data Should Not Be Empty")
    else:
        n1=int(name_entry1.get())
        n2=int(name_entry2.get())
        msg.showinfo("Multiplication",f"{n1*n2}")
def div():
    if name_entry1.get()=="" or name_entry2.get()=="":
        msg.showinfo("Alert !!!","The Data Should Not Be Empty")
    else:
        n1=int(name_entry1.get())
        n2=int(name_entry2.get())
        msg.showinfo("Division",f"{n1/n2}")

heading=Label(root, text="Welcome To Calculator", font=('Arial 18'), fg="green", bg="orange")
heading.place(x=400,y=100)

name=Label(root, text="Enter Number 1 : ", font=('Arial 12'))
name.place(x=200,y=200)

name=Label(root, text="Enter Number 2 : ", font=('Arial 12'))
name.place(x=200,y=220)

name_entry1=Entry(root,)
name_entry1.place(x=330,y=200)

name_entry2=Entry(root,)
name_entry2.place(x=330,y=220)


validate1=Button(root, text="+", font=('Arial 12'), command=add)
validate1.place(x=200,y=250)

validate2=Button(root, text="-", font=('Arial 12'), command=sub)
validate2.place(x=250,y=250)

validate3=Button(root, text="*", font=('Arial 12'), command=mul)
validate3.place(x=300,y=250)

validate4=Button(root, text="/", font=('Arial 12'), command=div)
validate4.place(x=350,y=250)

