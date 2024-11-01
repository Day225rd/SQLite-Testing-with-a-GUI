import tkinter as tk

from tkinter import *

from tkinter import ttk

import sqlite3

con = sqlite3.connect('1database.db')
cur = con.cursor()

root =tk.Tk()
root.title("Feedback")
class FeedbackApp:
    def __init__(self,master):
        root.geometry('400x400')

        self.label1 = ttk.Label(master,text = "Welcome")
        self.label1.place(x = 100, y = 50)

        self.label1 = ttk.Label(master,text = "Please complete the following fields below")
        self.label1.place(x = 80, y = 70)

        self.btn1 = ttk.Button(master, text = "Submit Feedback", command = self.fbsubmit)
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

        self.submitButton = ttk.Button(master, text = "submit", command = self.fbsubmit)
        self.submitButton.config(command = self.buttontext() )
        self.submitButton.place(x=140,y=300)

        self.printdata = ttk.Button(master, text = "See past submissions")
        self.printdata.config(command = self.buttontext())
        self.printdata.place(x = 140, y = 340)

    def txtprint(self):
        textentry = self.txtfield1.get("1.0", "end-1c"), self.txtfield2.get(), self.txtfield3.get(), self.txtfield4.get()
        print(textentry)

    def buttontext(self):
        print()

    def fbsubmit(self):
        number = self.txtfield1.get("1.0", "end-1c")
        name = self.txtfield2.get()
        email = self.txtfield3.get()
        feedback = self.txtfield4.get()
        values = [number, name, email, feedback]
        cur.execute('''INSERT INTO Feedback
                    (number ,name ,email ,feedback) 
                    VALUES (?, ?, ?, ?)''', values)
    

        con.commit()

        print("Feedback submitted")

fbapp = FeedbackApp(root)
root.mainloop()
con.close()


#/////////////////////////////
# button1 = ttk.Button(root)
# button1.config(text="Click here")
# button1.grid()

