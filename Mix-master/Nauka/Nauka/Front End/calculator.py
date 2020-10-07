from tkinter import *

root = Tk()
root.title("Calculator")

entry_box = Entry(root, width=35, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=3, padx= 10, pady= 10)

#-------------------------------------------

def button_click(number):

    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(current) + str(number))

def button_clear():
    entry_box.delete(0,END)

def button_add():
    pass

#-------------------------------------------

button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button7.grid(row=1, column =0)

button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button8.grid(row=1, column =1)

button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button9.grid(row=1, column =2)

button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button4.grid(row=2, column =0)

button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button5.grid(row=2, column =1)

button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button6.grid(row=2, column =2)

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button1.grid(row=3, column =0)

button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button2.grid(row=3, column =1)

button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button3.grid(row=3, column =2)

button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button0.grid(row=4, column =0)

button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_clear.grid(row=4, column =1, columnspan=2)

button_plus = Button(root, text="+", padx=39, pady=20, command=button_add)
button_plus.grid(row=5, column =0)

button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: button_click())
button_equal.grid(row=5, column =1, columnspan=2)


root.mainloop()