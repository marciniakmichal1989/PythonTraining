from tkinter import *

class Window():
    def __init__(self):
        pass

    def main_menu(self):
        window = Tk()

        window.geometry("640x480")
        window.resizable(0, 0)

        window.title("Black Jack")

        l1 = Label(window, text="")


        b1 = Button(window, text='Button1', width=20)
        b1.pack(side=BOTTOM, anchor=E)
        b2 = Button(window, text='Button2', width=20)
        b2.pack(side=BOTTOM, anchor=W)


        window.mainloop()