from tkinter import*
import tkinter as tk
from tkinter import messagebox
import sys
import os
import signal
import time
from subprocess import  *
from cassandra.cluster import Cluster
from tkinter import ttk 

root=Tk()                               #Main window 
f=Frame(root)
frame3=Frame(root)
root.title("Public login - Police Record System")
root.geometry("830x395")
root.configure(background="Black")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

searchid = StringVar()
    
    
def clear_all():             #for clearing the entry widgets
    frame3.pack_forget()

    
    
def search_emp():     #can implement search by 1st name,last name,station id
    clear_all()
    emp_id=Label(frame3,text="Enter Complaint ID",bg="red",fg="white")   #to take user input to seach
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
    try:
        print(id0)
        dict1 = {}
        cluster = Cluster()
        session = cluster.connect('missingvehicles')
        session.execute('USE missingvehicles')
        rows = session.execute('select compno,status from close_complaint')
        for row in rows:
            dict1[row.compno]=row.status
        list1 = list(dict1.keys())
        rows1 = session.execute('Select copmno from register_complaint')
        for row in rows1:
            list1.append(row.copmno)
        print(list1)
        if(id0 not in list1):
            str1 = "NO SUCH COMPLAINT EXIST!!!"
        else:
            list2 = list(dict1.keys())
            if(id0 in list2):
                str1 = "Your Vehicle has been found, contact near by police station or you can check your phone for SMS."
            else:
                str1 = "Your vehicle is yet to be found or if you had already found plese contact nearby police staion to close complaint."
        T = Text(frame3, height = 20, width =50)
        T.grid(row=8,column=1,pady=10)
        T.insert(tk.END,"Complaint Number:\t")
        T.insert(tk.END,id0)
        T.insert(tk.END,'\n')
        T.insert(tk.END,"\nStatus:\n")
        T.insert(tk.END,str1)

        session.shutdown()
        
    except Exception as e:
        messagebox.showerror("Failed", "error occured ")
        print(e)

def back():
    root.destroy()
    import option_public
    

        
#Main window buttons and labels
        
label1=Label(root,text="TRACK COMPLAINT")
label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
label1.pack(fill=X)

label2=Label(f,text="Select an action: ",font=('bold',12), background="Black", fg="White")
label2.pack(side=LEFT,pady=10)
button1=Button(f,text="Track Complaint", background="Brown", fg="White", command=search_emp, width=8)
button1.pack(side=LEFT,ipadx=20,pady=10)
button10=Button(f,text="Back To Home", background="Brown", fg="White", command=back, width=8)
button10.pack(side=LEFT,ipadx=20,pady=10)

button6=Button(f,text="Close", background="Brown", fg="White", width=8, command=root.destroy)
button6.pack(side=LEFT,ipadx=20,pady=10)
f.configure(background="Black")
f.pack()

root.mainloop()
