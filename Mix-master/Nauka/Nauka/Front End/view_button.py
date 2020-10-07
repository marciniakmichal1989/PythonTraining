from tkinter import *


root = Tk()

# Def Part :

def myClick():
    my_laabel = Label(root, text="You clicked me")
    # my_laabel.grid(row=3, column=0)
    my_laabel.pack()

# Label Part :

# myLabel1 = Label(root, text="Hello W")
# myLabel2 = Label(root, text="My name is Michal")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

#-----------------------------

# Button Part :

button1 = Button(root, text="Push me", padx=50, pady=10, fg="blue", bg="red", command=myClick)
# state=DISABLED - can not be used
# button1.grid(row=2, column=3)
button1.pack()

#-----------------------------

root.mainloop()
