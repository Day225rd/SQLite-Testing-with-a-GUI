import tkinter

from tkinter import *

from tkinter import ttk

root =Tk()
class FeedbackApp:
    def __init__(self,master):
        self.label1 = ttk.label(master,text = "Click here")
        self.label1.grid()

# button1 = ttk.Button(root)
# button1.config(text="Click here")
# button1.grid()

root.mainloop()