from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  call
import datetime

class Home():
    def __init__(self,master):
        try:
            with open('public_login_details.txt', 'r') as f:
                lines = f.read().splitlines()
                self.username = lines[-2]
                print(self.username)
        except:
            messagebox.showerror("Failed","Unable to unlock root directory")

        
        
        menu = Menu(master)
        master.config(menu=menu)

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
        exit_button.add_command(label='Minimize',command=self.minimize)
        
        label1=Label(master,text="Public Home")
        label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        label1.pack(fill=X)
        text1 = "Welcome!!!"+self.username
        print(text1)
        username_label=Label(master,text=text1,font=("Courier", 18))
        username_label.config(font=('Courier',18,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        username_label.pack(fill = X)

        label2=Label(master,text="Select an action: ",font=('bold',14), background="Black", fg="White")
        label2.pack(fill=X)
        button1=Button(master,text="Register Complaint",font=('Italic',12,'bold'), background="Brown", fg="White", command=self.register, width=12)
        button1.pack(fill=X)
        button2=Button(master,text="Track a Complaint", font=('Italic',12,'bold'),background="Brown", fg="white", command=self.track, width=8)
        button2.pack(fill=X)
        button4=Button(master,text="Log Out",font=('Italic',16,'bold'), background="Brown", fg="White", width=8, command=self.logout)
        button4.pack(fill=X)
        
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

    def track(self):
        print('Track Complaint')
        root.destroy()
        import track_complaint
        
    def register(self):
        print('Register')
        root.destroy()
        import register_complaint
    
    def logout(self):
        f = open("public_login_details.txt", "r+") 
        f.seek(0)
        f.truncate() 
        root.destroy()
        import Loginnpage

root = Tk()
f = Frame(root)
f.configure(background="Black")
f.pack()
public_login_home=Home(root)
root.wm_geometry("300x300")
root.configure(background = "black")
root.title("Public Login")
root.mainloop()
