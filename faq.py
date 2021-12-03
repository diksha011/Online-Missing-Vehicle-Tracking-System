import tkinter as tk
from tkinter import ttk 
import os
import signal
import tkinter.font as font

#Questions
q1 = "How MVTS can help you?"
a1 = """There is an increase in theft of vehicles now a days which result in great disturbance to the owners as they have to make frequent trips to the police station which is very time consuming and also is not very pocket friendly. Also for police department to entertain such cases is very difficult and also requires more man power as for completing the formalities and papers before handling the vehicle to legitimate owner they require a experienced police officer to eliminate mistakes in such procedures.
Online missing vehicle tracking system aims at reducing the trips and work for finding the missing vehicles for both police department and owner of such vehicles by reducing significantly the paperwork through simple centralized SMS sending services."""

q2 = "Do I have to have a cell phone or purchase cell service as well as MVTS service?"
a2 = "You can receive alerts to your cell phone identifying what the alert is for and the location of the vehicle."

q3 = "What if somebody tampers with the vehicle device?"
a3 = "In case if any such thing happen vehicle can be identified by using the proof of vehicle you will upload during registration."

q4 = "What kind of computer system do I need to Use MVTS?"
a4 = "The only requirement for using MVTS is a computer that supports Microsoft Internet Explorer 7, or later, or any equivalent browser."

q5 = "For how long do I have access to my data?"
a5 = "You can access the software as public as long as your complaint status is open"

dict1 = {q1:a1,q2:a2,q3:a3,q4:a4,q5:a5}

#Frame
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
        
        ##login frame starts here
        myFont = font.Font(size=16,weight=font.BOLD, family='Helvetica')
        myFont1 = font.Font(size=12, family='Helvetica')
        frame = Frame(master)
        Label1 = Label(master, text='Question:')
        Label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        Label1.pack(padx=15, pady=5)
        self.queschoosen = ttk.Combobox(master,state="readonly", width =77,values = list(dict1.keys()))
        self.queschoosen.pack(padx=15, pady=5)        
        self.queschoosen.bind('<<ComboboxSelected>>', self.getUpdateData)
        Label2 = Label(master, text='Answer:')
        Label2.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
        Label2.pack(padx=15, pady=5)
        self.T = Text(master, height = 15, width = 60,font  = myFont1)
        self.T.pack(padx=25, pady=5)
        
        btn = Button(frame, text='Close', background="Brown", fg="White",font = myFont, command=self.login_submit)
        btn.pack(fill = X)
        frame.pack(padx=100, pady=19)
        
    def getUpdateData(self,event):
        self.var1 = dict1[self.queschoosen.get()]
        self.T.insert(tk.END, self.var1)
        

    def login_submit(self):
        file_previous_close()
        root.destroy()
        print("Closed")

root=Tk()
login_home=Home(root)
root.wm_geometry("800x500")
root.title("FAQS")
root.configure(background = "tan")
root.mainloop()