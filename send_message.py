from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  call
import  xlrd
import xlwt
from cassandra.cluster import Cluster
import datetime

class Home():
    def __init__(self,master):
        self.date = datetime.date.today()
        

        #message box code


        message_label=Label(master,text="   Message to All Police Stations:   ",font=("Courier", 30),background="Orange",fg="Yellow")
        message_label.grid(row=0,column=0)
        self.message_variable=StringVar()
        large_font = ('Verdana', 24)
        message_entry = Entry(master, textvariable=self.message_variable, bd=10, font=large_font)
        message_entry.grid(row=4,column=0)
        message_submit=Button(master,text='Send to all the Police Stations',font=("Courier", 18),command=self.send_message,background="Brown", fg="White")
        message_submit.grid(row=8,column=0)
        button=Button(master,text='Back To admin',font=("Courier", 18),command=self.back,background="Brown", fg="White")
        button.grid(row=10,column=0)
        
    def back(self):
        root.destroy()
        import admin_login_success


    def send_message(self):
        message_value=self.message_variable.get()
        date=self.date
        print(date,message_value)
        try:
            cluster = Cluster()
            session = cluster.connect('missingvehicles')
            session.execute('USE missingvehicles')
            session.execute("INSERT into message(message,sent_date) values(%s,%s) ",(message_value,date))
            session.shutdown() 
            messagebox.showinfo("Message Sent","Your Message has been Sent")
        except:
            messagebox.showinfo("Error","Internal Servor Error Occured")




root=Tk()
admin_login_home=Home(root)
root.wm_geometry("1000x250")
root.configure(background = "black")
root.title("Admin Login - Send message")
root.mainloop()
