from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
from cassandra.cluster import Cluster

def file_previous_close():
    try:
        with open('home_id.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            page=lines[-2]
            if(page!='login'):
                os.kill(int(last_line),signal.SIGKILL)
    except:
        print('first instance no need to close previous file')

#file_previous_close()

def writing_id():
    file_home_id=open("home_id.txt","w+")
    home_id=os.getpid()
    file_home_id.writelines('login\n')
    file_home_id.writelines(str(home_id))
    file_home_id.close()
    print(home_id)

writing_id()


class Home():
    
    def __init__(self,master):
        menu = Menu(master)
        master.config(menu=menu, background = "brown")

        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='Take a Tour!!',command=self.take_a_tour)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
        home.add_separator()


        submenu = Menu(menu)
        menu.add_cascade(label='Help!!!', menu=submenu)
        submenu.add_command(label='Contact Us!',command=self.contact_us)
        submenu.add_command(label='FAQs', command=self.faq)
        submenu.add_command(label='Report Infringement', command=self.report_infringement)
        submenu.add_separator()

        about_us=Menu(menu)
        menu.add_cascade(label='About Us',menu=about_us)
        about_us.add_command(label='About us',command=self.about_us)
        about_us.add_separator()


        exit_button=Menu(menu)
        menu.add_cascade(label='Exit',menu=exit_button)
        exit_button.add_command(label='Exit',command=root.destroy)

        #can do a prompt to do yes or  no


        exit_button.add_command(label='Minimize',command=self.minimize)


        ##login frame starts here

        frame = Frame(master)
        self.var1 = StringVar()
        self.var2 = StringVar()

        Label1 = Label(master, text='Username:')
        Label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        Label1.pack(padx=15, pady=5)

        entry1 = Entry(master, bd=5,textvariable=self.var1)
        entry1.pack(padx=15, pady=5)

        Label2 = Label(master, text='Password: ')
        Label2.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        Label2.pack(padx=15, pady=6)

        entry2 = Entry(master,show="*" ,bd=5,textvariable=self.var2)
        entry2.pack(padx=15, pady=7)

        btn = Button(frame, text='Check Login', background="Brown", fg="White", command=self.login_submit)
        btn.pack(fill = X)
        frame.pack(padx=100, pady=19)
        
        btn = Button(frame, text='Change Password', background="Brown", fg="White", command=self.change)
        btn.pack(fill = X)
        frame.pack(padx=100, pady=19)
        
        btn1 = Button(frame, text='Login Option', background="Brown", fg="White", command=self.option)
        btn1.pack(fill = X)
        frame.pack(padx=100, pady=19)
        
    def option(self):
        root.destroy()
        import login_option

    def login_submit(self):
        file_previous_close()
        print("Attemted to login")
        self.username=int(self.var1.get())
        self.password=self.var2.get()
        print(self.username,self.password)
        try:
            dict1 = {}
            cluster = Cluster()
            session = cluster.connect('missingvehicles')
            session.execute('USE missingvehicles')
            rows = session.execute('SELECT username,password FROM police_record')
            for row in rows:
                dict1[row.username]=row.password
            if(dict1[self.username]==self.password):
                messagebox.showinfo("Login Success", "Taking You to Home Page")
                print("Welcome")
                root.destroy()
                import police_login_success
            else:
                print("Login failed")
                messagebox.showinfo("Login Failed", "Invalid Username or Password")            
        except Exception as e:
            messagebox.showinfo("Failed", "Error Occured")
            print(e)
            
    def change(self):
        root.destroy()
        import change_password
        
    
    def about_us(self):
        top = Toplevel()
        top.geometry("200x200")
        top.title("About Us")
        msg = Message(top, text='This Vehicle tracking system would help public and police department to track missing vehicle')
        msg.grid(row=0, column=15)
        button = Button(top, text="Dismiss", command=top.destroy)
        button.grid(row=4, column=15)

        ##declare a message box

    def faq(self):
        ##message box indicating faqs
        print('he')
        import faq

    def report_infringement(self):
        ##message box
        messagebox.showerror("Report Infringement","If found any infringement please mail us at 19bcs1557@gmail.com or call us at 9145879325")

    def take_a_tour(self):
        ##take a tour of the app
        import take_tour
        print('take a tour')

    def terms_of_use(self):
        string_terms="Privacy Statement Welcome MVTS. By accessing or using this Software, you (User or you) agree to comply with the terms and conditions governing your use of any areas of the MVTS.com web Software (the Software) as set forth below. USE OF Software Please read the Terms of Use (Terms) carefully before you start using the Software. By using the Software you accept and agree to be bound and abide by these Terms of Use and our Privacy Policy, found at incorporated herein by reference. If you do not agree to these Terms of Use or the Privacy Policy, you must not access or use the Software. This Software or any portion of this Software may not be reproduced, duplicated, copied, sold, resold, or otherwise exploited for any commercial purpose except as expressly permitted by MVTS.com, Inc. MVTS.com, Inc. and its affiliates reserve the right to refuse service, terminate accounts, and/or cancel orders in its discretion, including, without limitation, if MVTS.com, Inc. believes that User conduct violates applicable law or is harmful to the interests of MVTS.com, Inc. or its affiliates."
        dialog=Toplevel()
        dialog.geometry("400x400")
        dialog.title("Terms of Use")
        message=Message(dialog,text=string_terms)
        message.grid(row=0,column=0)
        button = Button(dialog, text="Close", command=dialog.destroy)
        button.grid(row=4, column=0)

    def contact_us(self):
        messagebox.showerror("Contact us ","In case of any dicrepancy or misbehaving of software Please contact us immediately.You can mail us at 19bcs1557@gmail.com or call us at 9145879325 ")

    def minimize(self):
        print('minimize the window')
        root.wm_state("iconic")



root=Tk()
login_home=Home(root)
root.wm_geometry("500x300")
root.title("Station Login")
root.configure(background = "tan")
root.mainloop()
