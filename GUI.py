import tkinter

from tkinter import *

from tkinter import ttk

root =Tk()
class FeedbackApp:
    def __init__(self,master):
        root.geometry('400x400')
        self.label1 = ttk.Label(master,text = "Welcome")
        self.label1.place(x = 200, y = 50)

        self.btn1 = ttk.Button(master, text = "Click Here")
        self.btn1.config(command = self.buttontext)
        self.btn1.place(x = 200, y = 200)

        self.field = ttk.Entry(master)
        self.field.place(x = 200, y = 250)

    def printinfo(self):
        print(self.field.get())

    def buttontext(self):
        print("TEST")

        self.btn1.config(text="BANG")
fbapp = FeedbackApp(root)
root.mainloop()



#/////////////////////////////
# button1 = ttk.Button(root)
# button1.config(text="Click here")
# button1.grid()

