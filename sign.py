from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
from tkinter.scrolledtext import ScrolledText
from cassandra.cluster import Cluster
import smtplib


def file_previous_close():
    try:
        with open('home_id.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            page=lines[-2]
            if(page!='registration'):
                os.kill(int(last_line),signal.SIGKILL)
    except:
        print('first instance no need to close previous file')

#file_previous_close()

def writing_id():
    file_home_id=open("home_id.txt","w+")
    home_id=os.getpid()
    file_home_id.writelines('registration\n')
    file_home_id.writelines(str(home_id))
    file_home_id.close()
    print('writing id')
    print(home_id)
def write_message_no(number):
    file=open("message.txt","w+")
    file.writelines(number)
    file.close()

def login_details(username,password):
    file=open("login_details.txt","w+")
    file.writelines(username+'\n')
    file.writelines(password)
    file.close()

#writing_id()


class Home():



    def __init__(self,master):

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

        #can do a prompt to do yes or  no


        exit_button.add_command(label='Minimize',command=self.minimize)
        
    

        ##Sign Up frame starts here

        frame = Frame(master)
        self.username = StringVar(master) #UserName
        self.password = StringVar()
        self.first_name=StringVar() #First name of User
        self.last_name = StringVar() #Last Name of User
        self.email=StringVar()
        self.mobile_number=StringVar()
        self.address_var=StringVar()
        
        
        first_name=Label(master,text="First Name:",bg="red",fg="white")
        first_name.pack(padx=15,pady=4)
        first_name_entry=Entry(master, bd=5,textvariable=self.first_name)
        first_name_entry.pack(padx=24,pady=4)
        
        last_name=Label(master,text="Last Name:",bg="red",fg="white")
        last_name.pack(padx=15,pady=4)
        last_name_entry=Entry(master, bd=5,textvariable=self.last_name)
        last_name_entry.pack(padx=24,pady=4)


        Label1 = Label(master, text='Username:',bg="red",fg="white")
        Label1.pack(padx=15, pady=5)
        entry1 = Entry(master, bd=5,textvariable=self.username)
        entry1.pack(padx=15, pady=5)


        email_label=Label(master,text='Email:',bg="red",fg="white")
        email_label.pack(padx=15,pady=6)
        email_entry=Entry(master,bd=5,textvariable=self.email)
        email_entry.pack(padx=15,pady=6)


        mobile_label=Label(master,text="Mobile:",bg="red",fg="white")
        mobile_label.pack(padx=15,pady=7)
        mobile_entry=Entry(master,bd=5,textvariable=self.mobile_number)
        mobile_entry.pack(padx=15,pady=7)

        Label2 = Label(master, text='Password: ',bg="red",fg="white")
        Label2.pack(padx=15, pady=9)
        entry2 = Entry(master,show="*" ,bd=5,textvariable=self.password)
        entry2.pack(padx=15, pady=9)

        address_label=Label(master,text='Address:',bg="red",fg="white")
        address_label.pack(padx=15,pady=10)

        large_font = ('Verdana', 30)
        address_entry=Entry(master,textvariable=self.address_var,bd=10,font=large_font)
        address_entry.pack(padx=15,pady=10)



        btn = Button(frame, text='Register',background="Brown", fg="White", command=self.register_submit)
        btn.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=19)
        

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
        ##message box indicating faqs

    def report_infringement(self):
        ##message box
        messagebox.showerror("Report Infringement","If found any infringement please mail us at 19bcs1557@gmail.com or call us at 9145879325")



    def take_a_tour(self):
        ##take a tour of the app
        import take_tour

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

    def register_submit(self):
        
        self.username_call=self.username.get()
        self.first_name_call=self.first_name.get()
        self.last_name_call=self.last_name.get()
        self.email_call=self.email.get()
        self.mobile_number_call=int(self.mobile_number.get())
        self.password_call=self.password.get()
        self.address_call=self.address_var.get()
            
        try:
            uName = []
            cluster = Cluster()
            session = cluster.connect('missingvehicles')
            session.execute('USE missingvehicles') 
            rows = session.execute("Select username from signup")
            for row in rows:
                uName.append(row.username)
            if(self.username_call in uName):
                counter = 0
                messagebox.showinfo("Failed", "Can't Register :( Username Occupied ")
            else:
                session.execute("INSERT INTO signup (username,address,email,fname,lname,mobile,password) values (%s,%s,%s,%s,%s,%s,%s)",(self.username_call,self.address_call,self.email_call,self.first_name_call,self.last_name_call,self.mobile_number_call,self.password_call))
                session.execute("INSERT INTO public_record (username,password)  values (%s,%s)",(self.username_call,self.password_call))
                session.shutdown()
                counter=1
                #sending email
                gmail_user = "missingvehicles96@gmail.com"
                gmail_pwd = "MissingVehicle123"
                TO = self.email_call
                SUBJECT = "Your Details After Registering With MVTS"
                TEXT = "Your Details are as:\nFirst Name: {}\nLast Name: {}\nUsername: {}\nPassword: {}\nMobile Number: {}\nAddress: {}\nThankyou for registring with MVTS.We hope you will find your vehicle soon.\nPlease do not revert back to this auto generated mail".format(self.first_name_call,self.last_name_call,self.username_call,self.password_call,self.mobile_number_call,self.address_call)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                BODY = '\r\n'.join(['To: %s' % TO,'From: %s' % gmail_user,'Subject: %s' 
                                % SUBJECT,'', TEXT])
                server.sendmail(gmail_user, [TO], BODY)
                print ('email sent')
        except Exception as e:
            counter=0
            messagebox.showinfo("Failed", "Can't Register")
            print(e)

        if(counter!=0):
            messagebox.showinfo("Successfully Registered","Taking you to the Login Page")
            root.destroy()
            import Loginnpage
            

   


root=Tk()
login_home=Home(root)
root.wm_geometry("500x1200")
root.configure(background = "tan")
root.title("SignUp Here")
root.mainloop()