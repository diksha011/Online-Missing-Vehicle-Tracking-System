from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
from tkinter.scrolledtext import ScrolledText
from cassandra.cluster import Cluster
import random

compList1 = []

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
        self.name = StringVar()
        self.Mobile = StringVar()
        self.dob = StringVar() #Date of Birth
        self.proof = StringVar()
        self.reg = StringVar()
        self.model = StringVar()
        self.type = StringVar()
        self.loc = StringVar()
        self.compNo = StringVar()
        
        Name=Label(master,text="Enter Name:",bg="red",fg="white")
        Name.pack(padx=15,pady=4)
        Name_entry=Entry(master, bd=5,textvariable=self.name)
        Name_entry.pack(padx=24,pady=4)
        
        mobile=Label(master,text="Enter Mobile Number:",bg="red",fg="white")
        mobile.pack(padx=15,pady=4)
        mobile_entry=Entry(master, bd=5,textvariable=self.Mobile)
        mobile_entry.pack(padx=24,pady=4)
        
        d_o_b=Label(master,text="Enter Date of Birth(yyyy-mm-dd):",bg="red",fg="white")
        d_o_b.pack(padx=15,pady=4)
        d_o_b_entry=Entry(master, bd=5,textvariable=self.dob)
        d_o_b_entry.pack(padx=24,pady=4)
        
        proofs=Label(master,text="Enter Licence Number:",bg="red",fg="white")
        proofs.pack(padx=15,pady=4)
        proof_entry=Entry(master, bd=5,textvariable=self.proof)
        proof_entry.pack(padx=24,pady=4)


        Label1 = Label(master, text='Vehicle Registration Number:',bg="red",fg="white")
        Label1.pack(padx=15, pady=4)
        entry1 = Entry(master, bd=5,textvariable=self.reg)
        entry1.pack(padx=15, pady=4)


        email_label=Label(master,text='Vehicle Model:',bg="red",fg="white")
        email_label.pack(padx=15,pady=4)
        email_entry=Entry(master,bd=5,textvariable=self.model)
        email_entry.pack(padx=24,pady=4)


        mobile_label=Label(master,text="Type Of Vehicle:",bg="red",fg="white")
        mobile_label.pack(padx=15,pady=4)
        self.type.set("Select Option")
        e4=OptionMenu(master,self.type,"Select Option", "2-Wheeler","4-Wheeler")
        e4.pack(padx=24,pady=4)

        Label2 = Label(master, text='Location Of Theft: ',bg="red",fg="white")
        Label2.pack(padx=15, pady=4)
        entry2 = Entry(master,bd=5,textvariable=self.loc)
        entry2.pack(padx=24, pady=4)        

        btn = Button(frame, text='Register Complaint',background="Brown", fg="White", command=self.register_submit)
        btn.pack(side=RIGHT, padx=5)
        
        btn1 = Button(frame, text='Back to Home Page',background="Brown", fg="White", command=self.Back)
        btn1.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=29)
        
    def Back(self):
        root.destroy()
        import option_public
        

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
        
        self.name_call = self.name.get()
        self.dob_call=self.dob.get()
        self.proof_call=self.proof.get()
        self.reg_call=self.reg.get()
        self.model_call=self.model.get()
        self.type_call=self.type.get()
        self.loc_call=self.loc.get()
        self.mobile_call = int(self.Mobile.get())
        print(self.name_call,self.dob_call,self.proof_call,self.reg_call)
        print(self.model_call,self.type_call,self.loc_call)
            
        try:
            cluster = Cluster()
            session = cluster.connect('missingvehicles')
            session.execute('USE missingvehicles')
            rows = session.execute('select copmno from register_complaint')
            for row in rows:
                compList1.append(row.copmno)
            self.compNo = random.randint(10000,50000)
            while(self.compNo in compList1):
                self.compNo = random.randint(10000,50000)
            
            Label2 = Label(root, text='Complaint Number: ',bg="red",fg="white")
            Label2.pack(padx=15, pady=4)
            entry2 = Label(root,state = 'disable',bd=5,text=self.compNo)
            entry2.pack(padx=24, pady=4)
            
            session.execute("INSERT INTO register_complaint (copmno,dob,licence,loc,mobile,model,name,regno,type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.compNo,self.dob_call,self.proof_call,self.loc_call,self.mobile_call,self.model_call,self.name_call,self.reg_call,self.type_call))
            session.shutdown()
            counter=1
        except Exception as e:
            counter=0
            messagebox.showinfo("Failed", "Try again later")
            print(e)


        if(counter!=0):
            messagebox.showinfo("Success","Taking you to Home Page")
            root.destroy()
            import option_public
            

   


root=Tk()
login_home=Home(root)
root.wm_geometry("500x1200")
root.configure(background = "tan")
root.title("Register Complaint")
root.mainloop()
