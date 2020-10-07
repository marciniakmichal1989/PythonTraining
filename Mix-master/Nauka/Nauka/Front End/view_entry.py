from tkinter import *

root = Tk()


my_entry = Entry(root, width=50, borderwidth=10)
my_entry.pack()
my_entry.insert(0,"Enter your name")
my_entry.get()

def myClick():
    hello = "Hello " + my_entry.get()
    my_Label = Label(root, text=hello, bg="green", fg="red")

    #another way do do this same

    # my_Label = Label(root, text="Hello " + my_entry.get(),bg="green", fg="red")
    my_Label.pack()

button = Button(root, text="Enter your name", command=myClick)
button.pack()

root.mainloop()