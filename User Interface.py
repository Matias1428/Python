from tkinter import*

from sqlalchemy import column

def click_button1():
    text='hola'

#Create a window
root=Tk()

#Creating a label widget
myLabel=Label(root, text="Hello world")
myLabe2=Label(root, text="Myu name is Matias")

#Shoving it onto the screen
#myLabel.pack()
myLabel.grid(row=0, column=0)
myLabe2.grid(row=1, column=0)

##Creating a button
myBotton1=Button(root,text="Click ME!", padx=50, pady=50)
myBotton1.grid(row=3, column=0)
#Loop
root.mainloop()