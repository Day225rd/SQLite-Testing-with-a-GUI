import tkinter as tk

from tkinter import *

from tkinter import ttk

root =tk.Tk()
root.title("Feedback")
class FeedbackApp:
    def __init__(self,master):
        root.geometry('400x400')

        self.label1 = ttk.Label(master,text = "Welcome")
        self.label1.place(x = 100, y = 50)

        self.label1 = ttk.Label(master,text = "Please complete the following fields below")
        self.label1.place(x = 80, y = 70)

        self.btn1 = ttk.Button(master, text = "Submit Feedback")
        self.btn1.config(command = self.buttontext)
        self.btn1.place(x = 150, y = 220)

        self.label1 = ttk.Label(master,text = "Feedback:")
        self.label1.place(x = 30, y = 190)
        self.txtfield1 = tk.Text(master)
        self.txtfield1.place(x = 140, y = 190, width = 130, height = 80)

        self.label2 = ttk.Label(master,text = "Name:")
        self.label2.place(x = 30, y = 130)
        self.txtfield2 = ttk.Entry(master)
        self.txtfield2.place(x = 140, y = 130)

        self.label3 = ttk.Label(master,text = "Email:")
        self.label3.place(x = 30, y = 160)
        self.txtfield3 = ttk.Entry(master)
        self.txtfield3.place(x = 140, y = 160)

        self.label4 = ttk.Label(master,text = "Phone Number:")
        self.label4.place(x = 30, y = 100)
        self.txtfield4 = ttk.Entry(master)
        self.txtfield4.place(x = 140, y = 100)





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

