from tkinter import*
from tkinter import messagebox
import sys
import os
import signal
import time
from subprocess import  *
from cassandra.cluster import Cluster
from tkinter import ttk
from pass_gen import password 
import tkinter as tk


root=Tk()                               #Main window 
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
root.title("Admin login - Police Record System")
root.geometry("830x395")
root.configure(background="Black")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

firstname=StringVar()                    #Declaration of all variables
lastname=StringVar()
id=StringVar()
polSt=StringVar() #police station
st=StringVar() #state of police station
dist = StringVar() #District of police station
remove_id = StringVar() 
remove_firstname=StringVar()
remove_lastname=StringVar()
searchid = StringVar()


def pol_dict(id,fname,lname,polst,states,dist):      #To add a new entry  
    try:
        list1 = []
        cluster = Cluster()
        session = cluster.connect('missingvehicles')
        session.execute('USE missingvehicles')
        rows = session.execute("select pid from add_police_station")
        for row in rows:
            list1.append(row.pid)
        if(id not in list1):
            T = Text(frame1, height = 20, width =25)
            T.grid(row=8,column=1,pady=10)
            T.insert(tk.END,"Username:\t")
            T.insert(tk.END,id)
            T.insert(tk.END,"\nPassword:\t")
            T.insert(tk.END,password)
            print("done")  
            session.execute("INSERT INTO add_police_station (pid, fname,lname,district,state,area) values (%s,%s,%s,%s,%s,%s)",(id,fname,lname,dist,states,polst))
            session.execute("Insert INTO police_record (username,password) values (%s,%s)",(id,password))
            session.shutdown()
            messagebox.showinfo("Success", "Police Station added")
            counter=1
        else:
            counter = 0
            messagebox.showinfo("Failed", "Already Registered")        
    except:
        counter=0
        messagebox.showinfo("Failed", "Can't Register")
    
    
def add_entries():                       #to append all data and add entries on click the button
    i1 = int(id.get())
    
    f=firstname.get()
    f1=f.lower()
    
    l=lastname.get()
    l1=l.lower()
    
    d=dist.get()
    d1=d.lower()
    
    st1=st.get()
    de1=st1.lower()
    
    pol = polSt.get()
    pols = pol.lower()
    pol_dict(i1,f1,l1,pols,de1,d1)


def add_info():                                           #for taking user input to add the enteries
    frame2.pack_forget()
    frame3.pack_forget()
    emp_id=Label(frame1,text="Enter ID of the Police Station: ",bg="red",fg="white")
    emp_id.grid(row=0,column=1,padx=10)
    e0=Entry(frame1,textvariable=id)
    e0.grid(row=0,column=2,padx=10)
    e0.focus()
    emp_first_name=Label(frame1,text="Enter first name of the Officer: ",bg="red",fg="white")
    emp_first_name.grid(row=1,column=1,padx=10)
    e1=Entry(frame1,textvariable=firstname)
    e1.grid(row=1,column=2,padx=10)
    e1.focus()
    emp_last_name=Label(frame1,text="Enter last name of the Officer: ",bg="red",fg="white")
    emp_last_name.grid(row=2,column=1,padx=10)
    e2=Entry(frame1,textvariable=lastname)
    e2.grid(row=2,column=2,padx=10)
    emp_dept=Label(frame1,text="Enter State of Police station: ",bg="red",fg="white")
    emp_dept.grid(row=3,column=1,padx=10)
    e3=Entry(frame1,textvariable=st)
    e3.grid(row=3,column=2,padx=10)
    emp_desig=Label(frame1,text="Enter district of Police Station: ",bg="red",fg="white")
    emp_desig.grid(row=4,column=1,padx=10)
    e4=Entry(frame1,textvariable=dist)
    e4.grid(row=4,column=2,padx=10)
    pol_st=Label(frame1,text="Enter police station area: ",bg="red",fg="white")
    pol_st.grid(row=6,column=1,padx=10)
    e5=Entry(frame1,textvariable=polSt)
    e5.grid(row=6,column=2,padx=10)
    button4=Button(frame1,text="Add entries",command=add_entries)
    button4.grid(row=7,column=2,pady=10)   
   
    frame1.configure(background="Red")
    frame1.pack(pady=10)
    

    
def clear_all():             #for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

    
def remove_emp():                #for taking user input to remove enteries
    clear_all()
    emp_id=Label(frame2,text="Enter ID of Police Station",bg="red",fg="white")
    emp_id.grid(row=0,column=1,padx=10)
    e=Entry(frame2,textvariable=remove_id)
    e.grid(row=0,column=2,padx=10)
    e.focus()
    emp_first_name=Label(frame2,text="Enter first name of the Officer",bg="red",fg="white")
    emp_first_name.grid(row=1,column=1,padx=10)
    e6=Entry(frame2,textvariable=remove_firstname)
    e6.grid(row=1,column=2,padx=10)
    e6.focus()
    emp_last_name=Label(frame2,text="Enter last name of the Officer",bg="red",fg="white")
    emp_last_name.grid(row=2,column=1,padx=10)
    e7=Entry(frame2,textvariable=remove_lastname)
    e7.grid(row=2,column=2,padx=10)
    remove_button=Button(frame2,text="Click to remove",command=remove_entry)
    remove_button.grid(row=3,column=2,pady=10)
    frame2.configure(background="Red")
    frame2.pack(pady=10)

def remove_entry():  #to remove entry
    rsi = int(remove_id.get())
    print(rsi)
    rsf=remove_firstname.get().lower()
    print(rsf)
    rsl=remove_lastname.get().lower()
    print(rsl)
    try:
        cluster = Cluster()
        session = cluster.connect('missingvehicles')
        session.execute('USE missingvehicles')
        query = 'Delete from add_police_station where pid = {};'.format(rsi)
        session.execute(query)
        query1 = 'Delete from police_record where username = {}'.format(rsi)
        session.execute(query1)
        messagebox.showinfo("Done","Successfully removed the police station record")
        counter=1
    except:
        counter=0
        messagebox.showinfo("Failed", "No such employee exist")
    
    clear_all()
    
def search_emp():     #can implement search by station id
    clear_all()
    emp_id=Label(frame3,text="Enter ID of the Police Station",bg="red",fg="white")   #to take user input to seach
    emp_id.grid(row=1,column=1,padx=10)
    e8=Entry(frame3,textvariable=searchid)
    e8.grid(row=1,column=2,padx=10)
    e8.focus()
    search_button=Button(frame3,text="Click to search",command=search_entry)
    search_button.grid(row=3,column=2,pady=10)
    
    frame3.configure(background="Red")
    frame3.pack(pady=10)
    
def search_entry():
    id0 = int(searchid.get())
    search_database (id0)
    
def search_database(id0):
    print('Success')
    try:
        cluster = Cluster()
        session = cluster.connect('missingvehicles')
        session.execute('USE missingvehicles')
        query = 'Select fname,lname,area,district,state from add_police_station where pid = {};'.format(id0)
        store = session.execute(query)
        i = 0        
        first_name_head = Label(frame3, text='First name:', font=("Courier", 14),background="Orange",fg="Yellow")
        first_name_head.grid(row=9, column=0)
        last_name_head = Label(frame3, text='Last name:', font=("Courier", 14),background="Orange",fg="Yellow")
        last_name_head.grid(row=9, column=1)
        area_head = Label(frame3, text='Area:', font=("Courier", 14),background="Orange",fg="Yellow")
        area_head.grid(row=9, column=2)
        dist_head = Label(frame3, text='District:', font=("Courier", 14),background="Orange",fg="Yellow")
        dist_head.grid(row=9, column=3)
        state_head = Label(frame3, text='State:', font=("Courier", 14),background="Orange",fg="Yellow")
        state_head.grid(row=9, column=5)
        for row in store:
            first_name = Label(frame3, text=row.fname, font=("Courier", 12))
            first_name.grid(row=10 + i, column=0)
            last_name = Label(frame3, text=row.lname, font=("Courier", 12))
            last_name.grid(row=10 + i, column=1)
            pol_list= Label(frame3, text=row.area,font=("Courier",12))
            pol_list.grid(row=10+i,column=2)
            dist_list = Label(frame3, text=row.district,font=("Courier",12))
            dist_list.grid(row=10+i,column=3)
            state_list = Label(frame3, text=row.state,font=("Courier",12))
            state_list.grid(row=10+i,column=5)
            i = i+1
    except Exception as e:
        messagebox.showerror("Failed", "error occured ")

def back():
    root.destroy()
    import admin_login_success
    

        
#Main window buttons and labels
        
label1=Label(root,text="ADMIN RECORD SYSTEM")
label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
label1.pack(fill=X)

label2=Label(f,text="Select an action: ",font=('bold',12), background="Black", fg="White")
label2.pack(side=LEFT,pady=10)
button1=Button(f,text="Add", background="Brown", fg="White", command=add_info, width=8)
button1.pack(side=LEFT,ipadx=20,pady=10)
button2=Button(f,text="Remove", background="Brown", fg="white", command=remove_emp, width=8)
button2.pack(side=LEFT,ipadx=20,pady=10)
button1=Button(f,text="Search", background="Brown", fg="White", command=search_emp, width=8)
button1.pack(side=LEFT,ipadx=20,pady=10)
button10=Button(f,text="Back To Admin", background="Brown", fg="White", command=back, width=8)
button10.pack(side=LEFT,ipadx=20,pady=10)

f.configure(background="Black")
f.pack()

root.mainloop()
