from tkinter import*
from tkinter import messagebox
import sys
import os
import signal
import time
from subprocess import  *
from cassandra.cluster import Cluster
from tkinter import ttk
import random
from twilio.rest import Client

root=Tk()                               #Main window 
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
root.title("Police login - Police Record System")
root.geometry("830x395")
root.configure(background="Black")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

name = StringVar()
Mobile = StringVar()
dob = StringVar() #Date of Birth
proof = StringVar()
reg = StringVar()
model = StringVar()
type1 = StringVar()
loc = StringVar()
compNo = StringVar()
remove_Vehicleid = StringVar() 
status=StringVar()
vehicleid = StringVar()
vehicleType = StringVar()
compList1 = []


def pol_dict(Name,dob1,mobile,p1,r1,mod1,types1,locs):                   #To add a new entry and check if entry already exist in excel sheet
    print(Name,dob1,mobile,p1,r1,mod1,types1,locs)
    print("done")
    try:
        cluster = Cluster()
        session = cluster.connect('missingvehicles')
        session.execute('USE missingvehicles')
        rows = session.execute('select copmno from register_complaint')
        for row in rows:
            compList1.append(row.copmno)
        compNo = random.randint(10000,50000)
        while(compNo in compList1):
            compNo = random.randint(10000,50000)
        
        Label2 = Label(frame1, text='Complaint Number: ',bg="red",fg="white")
        Label2.grid(row=10,column=1,padx=10)
        entry2 = Label(frame1,state = 'disable',bd=5,text=compNo)
        entry2.grid(row=10,column=2,padx=10)
            
        session.execute("INSERT INTO register_complaint (copmno,dob,licence,loc,mobile,model,name,regno,type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(compNo,dob1,p1,locs,mobile,mod1,Name,r1,types1))
        session.shutdown()
        counter=1
    except Exception as e:
        counter=0
        messagebox.showerror("Failed", "Try again later")
        print(e)
        
    if(counter!=0):
        messagebox.showinfo("Success","Complaint Registered")    
    
def add_entries():                       #to append all data and add entries on click the button
    dob1 = dob.get()
    
    Name = name.get().lower()
    mobile = int(Mobile.get())
    
    p=proof.get()
    p1=p.lower()
    
    r=reg.get()
    r1=r.lower()
    
    mod=model.get()
    mod1=mod.lower()
    
    types=type1.get()
    types1=types.lower()
    
    loc1 = loc.get()
    locs = loc1.lower()
    pol_dict(Name,dob1,mobile,p1,r1,mod1,types1,locs)


def add_complaint():                                           #for taking user input to add the enteries
    frame2.pack_forget()
    frame3.pack_forget()
    
    Name=Label(frame1,text="Enter Name:",bg="red",fg="white")
    Name.grid(row=0,column=1,padx=10)
    Name_entry=Entry(frame1, bd=5,textvariable=name)
    Name_entry.grid(row=0,column=2,padx=10)
    
    d_o_b=Label(frame1,text="Enter Date of Birth(yyyy-mm-dd):",bg="red",fg="white")
    d_o_b.grid(row=1,column=1,padx=10)
    d_o_b_entry=Entry(frame1, bd=5,textvariable=dob)
    d_o_b_entry.grid(row=1,column=2,padx=10)
    
    mobile=Label(frame1,text="Enter Mobile Number:",bg="red",fg="white")
    mobile.grid(row=2,column=1,padx=10)
    mobile_entry=Entry(frame1, bd=5,textvariable=Mobile)
    mobile_entry.grid(row=2,column=2,padx=10)
        
    proofs=Label(frame1,text="Enter Licence Number:",bg="red",fg="white")
    proofs.grid(row=3,column=1,padx=10)
    proof_entry=Entry(frame1, bd=5,textvariable=proof)
    proof_entry.grid(row=3,column=2,padx=10)

    Label1 = Label(frame1, text='Vehicle Registration Number:',bg="red",fg="white")
    Label1.grid(row=4,column=1,padx=10)
    entry1 = Entry(frame1, bd=5,textvariable=reg)
    entry1.grid(row=4,column=2,padx=10)


    model_label=Label(frame1,text='Vehicle Model:',bg="red",fg="white")
    model_label.grid(row=5,column=1,padx=10)
    model_entry=Entry(frame1,bd=5,textvariable=model)
    model_entry.grid(row=5,column=2,padx=10)

    mobile_label=Label(frame1,text="Type Of Vehicle:",bg="red",fg="white")
    mobile_label.grid(row=6,column=1,padx=10)
    type1.set("Select Option")
    e4=OptionMenu(frame1,type1,"Select Option", "2-Wheeler","4-Wheeler")
    e4.grid(row=6,column=2,padx=10)

    Label2 = Label(frame1, text='Location Of Theft: ',bg="red",fg="white")
    Label2.grid(row=7,column=1,padx=10)
    entry2 = Entry(frame1,bd=5,textvariable=loc)
    entry2.grid(row=7,column=2,padx=10)
        
    
    button4=Button(frame1,text="Register Complaint",command=add_entries)
    button4.grid(row=9,column=2,padx=10) 
   
    frame1.configure(background="Red")
    frame1.pack(pady=10)
    

    
def clear_all():             #for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

    
def remove_complaint():                #for taking user input to remove enteries
    clear_all()
    emp_id=Label(frame2,text="Enter COMPLAINT Number",bg="red",fg="white")
    emp_id.grid(row=0,column=1,padx=10)
    e=Entry(frame2,textvariable=remove_Vehicleid)
    e.grid(row=0,column=2,padx=10)
    e.focus()
    emp_first_name=Label(frame2,text="Status of Complaint",bg="red",fg="white")
    emp_first_name.grid(row=1,column=1,padx=10)
    status.set("Select Option")
    e6=OptionMenu(frame2,status,"Select Option", "Open","Close")
    e6.grid(row=1,column=2,padx=10)
    e6.focus()
    remove_button=Button(frame2,text="Click to Update",command=remove_entry)
    remove_button.grid(row=3,column=2,pady=10)
    frame2.configure(background="Red")
    frame2.pack(pady=10)

def remove_entry():  #to remove entry 
    rsi = int(remove_Vehicleid.get())
    rsf=status.get()
    rsf1=rsf.lower()
    print(rsf1)    
    try:
        list1 = []
        cluster = Cluster()
        session = cluster.connect('missingvehicles')
        session.execute('USE missingvehicles')
        rows = session.execute('select copmno from register_complaint')
        for row in rows:
            list1.append(row.copmno)           
        
        if(rsi in list1):
            que = 'Select mobile from register_complaint where copmno = {}'.format(rsi)
            res = session.execute(que)
            for result in res:
                number = result.mobile
            query = 'Delete from register_complaint where copmno = {};'.format(rsi)
            session.execute(query)
            session.execute('Insert into close_complaint(compno,status) values (%s,%s)',(rsi,rsf1))
            session.shutdown()
            
            fin_number = '+91'+str(number)
            
            account_sid = 'AC35a1a9549145aeba1ff8014b8ee6c5cc'
            auth_token = '72b7aaf9067022b56831af944b7ae5b5'
            client = Client(account_sid, auth_token)
            message = client.messages.create(body='Your Vehicle has been found.Kindly Contact nearby Police Station for more details.', from_='+12025090074'
            , to=fin_number)
            print(message.sid)
            
            messagebox.showinfo("Done","Successfully closed Complaint")
            counter=1
        else:
            counter=0
            messagebox.showinfo("Failed", "No such complaint available")
            
    except Exception as e:
        counter=0
        messagebox.showerror("Failed", "Internal Error")
        print(e)
    
    clear_all()
    
def new_complaint():     #can implement search by 1st name,last name,station id
    clear_all()
    vehicle_id=Label(frame3,text="Enter Vehicle Number",bg="red",fg="white")   #to take user input to add
    vehicle_id.grid(row=1,column=1,padx=10)
    e8=Entry(frame3,textvariable=vehicleid)
    e8.grid(row=1,column=2,padx=10)
    e8.focus()
    vehicle_type=Label(frame3,text="Enter Vehicle Type",bg="red",fg="white")   #to take user input to add
    vehicle_type.grid(row=2,column=1,padx=10)
    e8=Entry(frame3,textvariable=vehicleType)
    e8.grid(row=2,column=2,padx=10)
    e8.focus()
    search_button=Button(frame3,text="Click to Register",command=new_entry)
    search_button.grid(row=3,column=2,pady=10)
    
    frame3.configure(background="Red")
    frame3.pack(pady=10)
    
def new_entry():
    id0 = vehicleid.get()
    id1 = vehicleType.get()
    new_complaint_database (id0,id1)
    
def new_complaint_database(id0,id1):
    try:
        cluster = Cluster()
        session = cluster.connect('missingvehicles')
        session.execute('USE missingvehicles')
        session.execute('Insert into unknown_found (id,type) values (%s,%s)',(id0,id1))
        messagebox.showinfo('SUCCESS','ENTRY DONE')  
        clear_all()
       
    except Exception as e:
        messagebox.showerror("Failed", "error occured ")


    
def logout():
    root.destroy()
    import police_login
    

        
#Main window buttons and labels
        
label1=Label(root,text="STATION RECORD SYSTEM")
label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
label1.pack(fill=X)

label2=Label(f,text="Select an action: ",font=('bold',12), background="Black", fg="White")
label2.pack(side=LEFT,pady=10)
button1=Button(f,text="Register", background="Brown", fg="White", command=add_complaint, width=8)
button1.pack(side=LEFT,ipadx=20,pady=10)
button2=Button(f,text="Close Complaint", background="Brown", fg="white", command=remove_complaint, width=8)
button2.pack(side=LEFT,ipadx=20,pady=10)
button1=Button(f,text="New Missing Vehicle", background="Brown", fg="White", command=new_complaint, width=10)
button1.pack(side=LEFT,ipadx=20,pady=10)
button6=Button(f,text="Log Out", background="Brown", fg="White", width=8, command=logout)
button6.pack(side=LEFT,ipadx=20,pady=10)
f.configure(background="Black")
f.pack()

root.mainloop()
