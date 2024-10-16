import tkinter as tk
from tkinter import messagebox
import os

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Arsh" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome to the Restaurant Billing System!")
        root.destroy()
        os.system('python Order.py')  # Update the path to your main script if necessary
    else:
        messagebox.showerror("Login Error", "Invalid Username or Password")

# Create the main window
root = tk.Tk()
root.title(" ")
root.resizable(False, False)
root.geometry(f"1000x600+100+100")

# Adding background color
root.configure(bg="black")

# Load and display an image as a logo
photo = tk.PhotoImage(file='bg2.png')  # Update with your image path
logo_label = tk.Label(root, image=photo, bg="black")
logo_label.place(x=-10, y=130)

# Main Heading Label
heading_label = tk.Label(root, text="Restaurant Billing System", bg="black", fg="gold", font=("Helvetica", 24, "bold"))
heading_label.place(x=0, y=10, relwidth=1)

# Create a frame for the login form
login_frame = tk.Frame(root, bg="#444444", bd=5)  # Medium gray frame background
login_frame.place(x=580, y=150)

# Login Heading inside the frame
login_heading = tk.Label(login_frame, text="Login", bg="#444444", fg="white", font=("Helvetica", 16, "bold"))
login_heading.grid(row=0, columnspan=2, pady=10)

# Username Label and Entry
username_label = tk.Label(login_frame, text="Username", bg="#444444", fg="white", font=("Helvetica", 12))
username_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')
username_entry = tk.Entry(login_frame, font=("Helvetica", 12), width=25, bd=2)
username_entry.grid(row=1, column=1, padx=20, pady=10)

# Password Label and Entry
password_label = tk.Label(login_frame, text="Password", bg="#444444", fg="white", font=("Helvetica", 12))
password_label.grid(row=2, column=0, padx=20, pady=10, sticky='w')
password_entry = tk.Entry(login_frame, show='*', font=("Helvetica", 12), width=25, bd=2)
password_entry.grid(row=2, column=1, padx=20, pady=10)

# Login Button
login_button = tk.Button(root, text="Login", command=login, bg="#5DADE2", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5, width=10)
login_button.place(x=850, y=320)

# Run the application
root.mainloop()
