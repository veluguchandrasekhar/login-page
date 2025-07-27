import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create the database (if it doesn't exist)
def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY, 
                        password TEXT)''')
    conn.commit()
    conn.close()

# Function to register a new user
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Registration", "User registered successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Function to validate login
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place labels and entry fields
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Create and place buttons
button_login = tk.Button(root, text="Login", command=login_user)
button_login.grid(row=2, column=0, padx=10, pady=10)

button_register = tk.Button(root, text="Register", command=register_user)
button_register.grid(row=2, column=1, padx=10, pady=10)

# Create the database when the script starts
create_db()

# Run the application
root.mainloop()
