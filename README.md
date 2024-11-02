Done without the use of generative AI for DS-3850. But with the help Stackoverflow, GeeksforGeeks, SQLite syntax. 

Lines like 3 are the title lines, the indented lines are the explanation.
Very fun project, has been my favorite so far. 


Database Connection
	con = sqlite3.connect('newDB.db'): Creates a connection to the SQLite database named newDB.db. If the database doesn't 			exist, it will be created.
	cur = con.cursor(): Creates a cursor object, cur, which allows executing SQL commands and interacting with the database.

Tkinter Root Window
	root = tk.Tk(): Initializes the main Tkinter window.
	root.title("Feedback"): Sets the window title to "Feedback".

FeedbackApp Class
	class FeedbackApp:: Defines a class named FeedbackApp to encapsulate all components of the feedback application.
	def __init__(self, master):: Initializes the class with master as the parent window (the root window passed when 		 
	instantiating FeedbackApp).
	root.geometry('400x400'): Sets the window size to 400x400 pixels.

Labels and Buttons
	ttk.Label: Creates a label widget with the given text.
	.place(x=, y=): Places the widget at specific x and y coordinates in the window.
	Similarly, additional labels are created for feedback, name, email, and phone number fields, along with corresponding 			entry fields using ttk.Entry (single-line input) or tk.Text (multi-line input)

Submit Button
	ttk.Button: Creates a button widget labeled "Submit Feedback".
	command=self.fbsubmit: Assigns the fbsubmit function to be called when the button is clicked.
	.config(command=self.buttontext): Overrides the previous command and assigns the buttontext method instead. 
	.place(x=, y=): Places the button at specific coordinates

fbhistorypassword Method
	def fbhistorypassword(self):: Defines a method for checking a password before allowing access to past entries.
	input("Please enter the password ->"): Prompts the user to input a password.
	if password == "1":: Checks if the input matches the correct password, "1". If correct, calls the history method.
	else: Prints "Incorrect password" if the password is incorrect.

history Method
	def history(self):: Defines a method to display past feedback entries.
	cur.execute('SELECT * FROM feedback'): Executes an SQL command to select all records from the feedback table.
	print(cur.fetchall()): Prints all rows retrieved from the query as a list of tuples

txtprint and buttontext Methods
	txtprint: Gets text from the entry fields and prints them to the console.
	buttontext: Placeholder function that currently only prints an empty line

fbsubmit Method
	def fbsubmit(self):: Defines the function for inserting feedback data into the database.
	self.txtfield4.get(): Retrieves text input for phone number.
	values = [...]: Stores the inputs in a list.
	cur.execute(...): Inserts the data into the feedback table.
	con.commit(): Commits the changes to the database, saving the new record.

Application Execution
	fbapp = FeedbackApp(root): Instantiates FeedbackApp with root as the main window.
	root.mainloop(): Runs the Tkinter event loop, keeping the application window open.
	con.close(): Closes the databa





























































