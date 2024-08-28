import tkinter as tk
from tkinter import ttk
from .widgets import DataTable
from utils.db_helper import fetch_data

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill='both', expand=True)

        self.table = DataTable(self.frame)
        self.table.pack(fill='both', expand=True)
        self.load_data()

    def load_data(self):
        data = fetch_data()
        self.table.update_data(data)
