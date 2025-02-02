import tkinter as tk
import random
import string
from tkinter import messagebox
def generate():
    length = length_entry.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Error", "Please enter a valid positive number")
        return    
    length = int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
#  main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
# Label
tk.Label(root, text="Enter Password Length:").pack(pady=5)
# Entry field
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
# Button
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack(pady=10)
# Password display
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, state='readonly', width=30)
password_entry.pack(pady=5)

# Run the application
root.mainloop()
