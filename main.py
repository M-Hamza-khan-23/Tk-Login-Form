import tkinter
from tkinter import messagebox

# Create the main window
window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='black')

# Function to handle login button click
def login():
    username = "Hamza"
    password = "12345"
    # Get the text entered in username and password entry fields
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    if entered_username == username and entered_password == password:
        # Show a success message box if credentials are correct
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        # Show an error message box if credentials are incorrect
        messagebox.showerror(title="Error", message="Invalid login.")

# Create a frame within the window for organizing widgets
frame = tkinter.Frame(window, bg='black')

# Creating Widgets (labels, entries, button)
login_label = tkinter.Label(frame, text="Login", bg='black', fg='white', font=("Arial", 30))
username_label = tkinter.Label(frame, text="UserName", bg='black', fg='white', font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='black', fg="white", font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg='salmon', fg='white', font=("Arial", 16), command=login)

# Grid placement of widgets within the frame
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=45)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=25)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=25)
login_button.grid(row=3, column=0, columnspan=2, pady=35)

# Pack the frame to place it in the window
frame.pack()

# Start the tkinter main loop
window.mainloop()
