import tkinter as tk
from tkinter import messagebox
def addtask():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")
def removetask():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")
def savetasks():
    with open("tasks.txt", "w") as file:
        tasks = tasks_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")
# Creating main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
# Input
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
# Buttons
add_button = tk.Button(root, text="Add Task", command=addtask)
add_button.pack()
remove_button = tk.Button(root, text="Remove Task", command=removetask)
remove_button.pack()
save_button = tk.Button(root, text="Save Tasks", command=savetasks)
save_button.pack()
# Task listbox
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)
# Run 
root.mainloop()
