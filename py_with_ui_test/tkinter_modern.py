import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Modern To-Do List")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

title_label = ttk.Label(root, text="To-Do List", font=("Helvetica", 18))
title_label.pack(pady=10)

task_entry = ttk.Entry(root, width=30)
task_entry.pack(pady=10)

task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass

add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
