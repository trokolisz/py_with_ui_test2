from tkinter import ttk

def apply_styles():
    style = ttk.Style()
    style.configure('Treeview', background='#f0f0f0', foreground='black', font=('Arial', 10))
    style.configure('Treeview.Heading', background='#d0d0d0', font=('Arial', 12, 'bold'))
