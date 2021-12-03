from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
from cassandra.cluster import Cluster

class Home():
    
    def __init__(self,master):
        ##login frame starts here

        frame = Frame(master)
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.type = StringVar()
        
        mobile_label=Label(master,text="Type Of Account:",bg="red",fg="white")
        mobile_label.pack(padx=15,pady=4)
        self.type.set("Select Option")
        e4=OptionMenu(master,self.type,"Select Option","Public","Police Station")
        e4.pack(padx=24,pady=4)
        
        Label0 = Label(master, text='ID:')
        Label0.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        Label0.pack(padx=15, pady=5)

        self.entry1 = Entry(master, bd=5,textvariable=self.var3)
        self.entry1.pack(padx=15, pady=5)

        Label1 = Label(master, text='New Password:')
        Label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        Label1.pack(padx=15, pady=5)

        self.entry1 = Entry(master,show = "*", bd=5,textvariable=self.var1)
        self.entry1.pack(padx=15, pady=5)

        Label2 = Label(master, text='Confirm Password: ')
        Label2.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        Label2.pack(padx=15, pady=6)

        self.entry2 = Entry(master,show="*" ,bd=5,textvariable=self.var2)
        self.entry2.pack(padx=15, pady=7)

        btn = Button(frame, text='Change Password', background="Brown", fg="White", command=self.login_submit)
        btn.pack(fill = X)
        frame.pack(padx=100, pady=19)

    def login_submit(self):
        self.passw=self.var1.get()
        self.password=self.var2.get()
        self.username = self.var3.get()
        self.account = self.type.get()
        
        print(self.passw,self.password)
        if(self.passw==self.password):
            try:
                cluster = Cluster()
                session = cluster.connect('missingvehicles')
                session.execute('USE missingvehicles')
                if(self.account=='Police Station'):
                    user = []
                    rows = session.execute('select username from police_record')
                    for row in rows:
                        user.append(row.username)                    
                    u = int(self.username)
                    if(u in user):
                        session.execute('INSERT INTO police_record (username,password) values (%s,%s)',(u,self.password))
                        messagebox.showinfo("SUCCESS", "PASSWORD CHANGED")
                        root.destroy()
                        import police_login
                    else:
                        messagebox.showinfo("FAIL", "NO SUCH USER EXIST")
                        self.entry1.delete(0,'end')
                        self.entry2.delete(0,'end')
                elif(self.account == 'Public'):
                    user1 = []
                    rows = session.execute('select username from public_record')
                    for row in rows:
                        user1.append(row.username)
                    if(self.username in user1):
                        session.execute('INSERT INTO public_record (username,password) values (%s,%s)',(self.username,self.password))
                        messagebox.showinfo("SUCCESS", "PASSWORD CHANGED")
                        root.destroy()
                        import Loginnpage
                    else:
                        messagebox.showinfo("FAIL", "NO SUCH USER EXIST")
                else:
                    messagebox.showinfo("FAILED", "SELECT TYPE OF ACCOUNT")
                    self.entry1.delete(0,'end')
                    self.entry2.delete(0,'end')
                    
            except Exception as e:
                messagebox.showinfo("Failed", "Can't connect to the server")
                print(e)
            
        else:
            print("Error")
            messagebox.showinfo("Failed", "Password does not match")
            self.entry1.delete(0,'end')
            self.entry2.delete(0,'end')


root=Tk()
login_home=Home(root)
root.wm_geometry("500x400")
root.title("Password Change")
root.configure(background = "tan")
root.mainloop()
