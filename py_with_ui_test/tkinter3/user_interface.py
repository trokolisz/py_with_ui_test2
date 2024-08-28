import tkinter as tk
from tkinter import ttk
from data import UserData
from permissions import PermissionsWindow
from settings import Settings
from typing import Optional, List, Dict
from exceptions import UserNotFoundError
from logger import setup_logger

logger = setup_logger()

class UserInterface:
    def __init__(self, root: tk.Tk, user_data: UserData) -> None:
        self.root = root
        self.user_data = user_data
        self.settings = Settings()
        self.open_windows = []
        self.displayed_columns = self.settings.selected_columns

        # Menu
        self.create_menu()

        # Search Entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=50)
        self.search_entry.pack(pady=10)
        self.search_var.trace("w", self.update_table)

        # Table
        self.tree = ttk.Treeview(root, columns=self.displayed_columns, show="headings")
        self.update_table_headers()
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree.bind("<ButtonRelease-1>", self.on_item_click)
        self.root.bind("<Button-1>", self.on_main_click)

        self.update_table()

    def create_menu(self) -> None:
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        self.column_vars = {}
        for column in ["ID", "Name", "Username", "Email", "Role", "Status", "Actions"]:
            var = tk.IntVar(value=1 if column in self.displayed_columns else 0)
            self.column_vars[column] = var
            view_menu.add_checkbutton(label=column, variable=var, command=self.update_displayed_columns)
        menu_bar.add_cascade(label="View", menu=view_menu)

    def update_displayed_columns(self) -> None:
        self.displayed_columns = [col for col, var in self.column_vars.items() if var.get() == 1]
        self.settings.update_selected_columns(self.displayed_columns)
        self.update_table_headers()
        self.update_table()

    def update_table_headers(self) -> None:
        self.tree["columns"] = self.displayed_columns
        for col in self.displayed_columns:
            self.tree.heading(col, text=col)

    def update_table(self, *args) -> None:
        try:
            search_value = self.search_var.get().lower()
            self.tree.delete(*self.tree.get_children())

            filtered_data = self.user_data.search_users(search_value)
            for row in filtered_data:
                values = tuple(row[col.lower()] if col.lower() in row else "Enabled" if row["enabled"] else "Disabled"
                               if col == "Status" else "View Permissions" if col == "Actions" else ""
                               for col in self.displayed_columns)
                self.tree.insert("", tk.END, iid=row["id"], values=values)
        except Exception as e:
            logger.error(f"Error updating table: {e}")

    def on_item_click(self, event: tk.Event) -> None:
        try:
            item_id = self.tree.identify_row(event.y)
            col = self.tree.identify_column(event.x)
            if item_id and col == f"#{self.displayed_columns.index('Actions') + 1}":  # Actions column index
                x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()
                permissions = self.user_data.get_permissions(item_id)
                self.show_permissions(x, y, item_id, permissions)
        except UserNotFoundError as e:
            logger.error(f"User not found: {e}")
        except Exception as e:
            logger.error(f"Error handling item click: {e}")

    def on_main_click(self, event: tk.Event) -> None:
        self.close_all_windows()

    def show_permissions(self, x: int, y: int, user_id: str, permissions: List[str]) -> None:
        try:
            permissions_window = PermissionsWindow(self.root, user_id, permissions, self.user_data)
            permissions_window.show(x, y)
            self.open_windows.append(permissions_window)
        except Exception as e:
            logger.error(f"Error showing permissions: {e}")

    def close_all_windows(self) -> None:
        for window in self.open_windows:
            window.close()
        self.open_windows.clear()
