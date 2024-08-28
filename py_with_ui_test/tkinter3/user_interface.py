import tkinter as tk
from tkinter import ttk
from data import UserData
from permissions import PermissionsWindow
from typing import Optional
from exceptions import UserNotFoundError

class UserInterface:
    def __init__(self, root: tk.Tk, user_data: UserData) -> None:
        self.root = root
        self.user_data = user_data
        self.open_windows = []

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=50)
        self.search_entry.pack(pady=10)
        self.search_var.trace("w", self.update_table)

        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Username", "Status", "Actions"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Actions", text="Actions")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree.bind("<ButtonRelease-1>", self.on_item_click)
        self.root.bind("<Button-1>", self.on_main_click)
        
        self.update_table()

    def update_table(self, *args) -> None:
        try:
            search_value = self.search_var.get().lower()
            self.tree.delete(*self.tree.get_children())

            filtered_data = self.user_data.search_users(search_value)
            for row in filtered_data:
                self.tree.insert("", tk.END, iid=row["id"], values=(
                    row["id"],
                    row["name"],
                    row["username"],
                    "Enabled" if row["enabled"] else "Disabled",
                    "View Permissions"
                ))
        except Exception as e:
            print(f"Error updating table: {e}")

    def on_item_click(self, event: tk.Event) -> None:
        try:
            item_id = self.tree.identify_row(event.y)
            col = self.tree.identify_column(event.x)
            if item_id and col == "#5":
                x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()
                permissions = self.user_data.get_permissions(item_id)
                self.show_permissions(x, y, item_id, permissions)
        except UserNotFoundError as e:
            print(f"User not found: {e}")
        except Exception as e:
            print(f"Error handling item click: {e}")

    def on_main_click(self, event: tk.Event) -> None:
        self.close_all_windows()

    def show_permissions(self, x: int, y: int, user_id: str, permissions: list[str]) -> None:
        try:
            permissions_window = PermissionsWindow(self.root, user_id, permissions, self.user_data)
            permissions_window.show(x, y)
            self.open_windows.append(permissions_window)
        except Exception as e:
            print(f"Error showing permissions: {e}")

    def close_all_windows(self) -> None:
        for window in self.open_windows:
            window.close()
        self.open_windows.clear()
