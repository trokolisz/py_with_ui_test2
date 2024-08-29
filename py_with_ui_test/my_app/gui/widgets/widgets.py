import tkinter as tk
from tkinter import ttk

class DataTable(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent, columns=("ID", "Name", "Value"), show='headings')
        self.heading("ID", text="ID")
        self.heading("Name", text="Name")
        self.heading("Value", text="Value")

    def update_data(self, data):
        self.delete(*self.get_children())
        for row in data:
            self.insert("", "end", values=row)
