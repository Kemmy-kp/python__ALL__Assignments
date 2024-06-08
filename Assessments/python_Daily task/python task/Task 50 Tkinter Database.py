from tkinter import *
from tkinter import messagebox as msg
import mysql.connector

root=Tk()
root.title('Student Portal')
root.geometry('500x550')
root.resizable(False,False)

# string var declaration for radiobutton
var=StringVar()

#===============================================================================

# database connection

def connect():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_sys"
        )

# function to insert data

def insert_data():
    if esid.get()=="" or ename.get()=="" or eage.get()=="" or var.get()=="":
        msg.showinfo("Insert status ","Data can't be blank")

    else:
        conn=connect()
        cursor=conn.cursor()
        query="insert into student values(%s,%s,%s,%s)"
        args=(esid.get(),ename.get(),eage.get(),var.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("Insert status ","Data Inserted Done")

# function to search data

def search_data():
    if esid.get()=="":
        msg.showinfo("Search status ","Id is Mandatory")

    else:
        conn=connect()
        cursor=conn.cursor()
        query="select * from student where id=%s"
        args=(esid.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        print(row)
        esid.delete(0,'end')
        ename.delete(0,'end')
        eage.delete(0,'end')
        for i in row:
            esid.insert(0,i[0])
            ename.insert(0,i[1])
            eage.insert(0,i[2])
        conn.commit()
        conn.close()
        


#query="delete from student where id=%s"
#args=(sid.get(),)
        
#query="update student set name=%s,age=%s,gender=%s where id=%s"

        
#query="select * from student where id=%s"

#================================================================================

#====================Labels=========================

head=Label(root, text="Student Management System", font=('Arial 16 bold'))
head.place(x=80,y=50)

sid=Label(root, text="Roll No : ", font=('Arial 12'))
sid.place(x=80,y=100)

name=Label(root, text="Enter Name : ", font=('Arial 12'))
name.place(x=80,y=150)

age=Label(root, text="Age : ", font=('Arial 12'))
age.place(x=80,y=190)

gender=Label(root, text="Gender : ", font=('Arial 12'))
gender.place(x=80,y=230)

#=========================Input=========================

esid=Entry(root,)
esid.place(x=180,y=100)

ename=Entry(root,)
ename.place(x=180,y=150)

eage=Entry(root,)
eage.place(x=180,y=190)

male=Radiobutton(root, text="male", variable=var,value="male")
male.place(x=180,y=230)

female=Radiobutton(root, text="female", variable=var,value="female")
female.place(x=250,y=230)

#====================Buttons====================
insert=Button(root,text="Insert", font=('Arial 12'),command=insert_data)
insert.place(x=100,y=270)

delete=Button(root,text="Delete", font=('Arial 12'))
delete.place(x=220,y=270)

update=Button(root,text="Update", font=('Arial 12'))
update.place(x=100,y=330)

search=Button(root,text="Search", font=('Arial 12'),command=search_data)
search.place(x=220,y=330)



root.mainloop()
