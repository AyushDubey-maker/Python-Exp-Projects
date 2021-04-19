from tkinter import *
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='mydatabase')
cursor=conn.cursor()

class next:
  def __init__(self,root):
     self.f=Frame(root,height=500,width=500)
     self.f.pack()
     self.b1=Button(self.f,text="Show",command=self.display)
     self.b1.place(x=200,y=150)
  def display(self):
     print ("----------View records-----------")
     #sql = "SELECT * FROM EMPLOYEE1 limit 0,10"
     cursor.execute("SELECT * FROM EMPLOYEE1 limit 0,10")
     i=0
     try:
        for d in cursor:
           for j in range(len(d)):
              e=Entry(self.f,width=10,fg='blue')
              e.grid(row=i,column=j)
              e.insert(END,d[j])
           i=i+1
     except Exception:
        print ("Error: unable to fecth data")


root=Tk()
root.title("Welcome To Next Window")
obj=next(root)
root.mainloop()
