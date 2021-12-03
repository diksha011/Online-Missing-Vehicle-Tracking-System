from tkinter import *
import tkinter.font as font


root=Tk()
# define font
myFont = font.Font(size=16,weight=font.BOLD, family='Helvetica')

photo = PhotoImage(file='tour.png')
Lower_frame=Frame(root)
label = Label(Lower_frame, image=photo)
label.image = photo
Button(root, text = 'OK',font = myFont,background="Brown", fg="White",height = 2,width = 5, command=root.destroy,compound = LEFT).pack(side = BOTTOM) 
label.pack()
Lower_frame.pack()
root.wm_geometry("852x550")
root.configure(background= "black")
root.title("Take a Tour")
root.mainloop()