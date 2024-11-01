import tkinter

from tkinter import *

from tkinter import ttk

root =Tk()
class FeedbackApp:
    def __init__(self,master):
        self.label1 = ttk.Label(master,text = "Welcome")
        self.label1.place(x=25,y=100)
        self.btn1 = ttk.Button(master, text = "Click Here")
        self.btn1.config(command = self.buttontext)
        self.btn1.place(x=20,y=150)
    def buttontext(self):
        print("TEST")
fbapp = FeedbackApp(root)
root.mainloop()



#/////////////////////////////
# button1 = ttk.Button(root)
# button1.config(text="Click here")
# button1.grid()

