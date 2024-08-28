import tkinter as tk
from tkinter import simpledialog
from data import UserData
from typing import List
from exceptions import PermissionError

class PermissionsWindow:
    def __init__(self, root: tk.Tk, user_id: str, permissions: List[str], data: UserData) -> None:
        self.root = root
        self.user_id = user_id
        self.permissions = permissions.copy()
        self.data = data
        self.window = tk.Toplevel(self.root)
        self.window.title("Permissions")
        self.create_widgets()

    def create_widgets(self) -> None:
        try:
            permissions_frame = tk.Frame(self.window)
            permissions_frame.pack(pady=10, fill=tk.BOTH, expand=True)

            canvas = tk.Canvas(permissions_frame)
            scrollbar = tk.Scrollbar(permissions_frame, orient="vertical", command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.inner_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            canvas.config(yscrollcommand=scrollbar.set)

            self.update_permissions_list()

            buttons_frame = tk.Frame(self.window)
            buttons_frame.pack(pady=10, fill=tk.X)

            add_button = tk.Button(buttons_frame, text="Add Permission", command=self.add_permission)
            add_button.pack(side=tk.BOTTOM, pady=10)

            self.inner_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
        except Exception as e:
            print(f"Error creating widgets: {e}")

    def update_permissions_list(self) -> None:
        try:
            for widget in self.inner_frame.winfo_children():
                widget.destroy()

            for perm in self.permissions:
                frame = tk.Frame(self.inner_frame)
                label = tk.Label(frame, text=perm)
                label.pack(side=tk.LEFT, padx=5, pady=5)

                delete_button = tk.Button(frame, text="X", command=lambda p=perm: self.delete_permission(p))
                delete_button.pack(side=tk.RIGHT, padx=5, pady=5)
                frame.pack(fill=tk.X)
        except Exception as e:
            print(f"Error updating permissions list: {e}")

    def add_permission(self) -> None:
        try:
            new_perm = simpledialog.askstring("Add Permission", "Enter new permission:")
            if new_perm and new_perm not in self.permissions:
                self.data.add_permission(self.user_id, new_perm)
                self.permissions.append(new_perm)
                self.update_permissions_list()
        except PermissionError as e:
            print(f"Permission error: {e}")
        except Exception as e:
            print(f"Error adding permission: {e}")

    def delete_permission(self, permission: str) -> None:
        try:
            if permission in self.permissions:
                self.data.remove_permission(self.user_id, permission)
                self.permissions.remove(permission)
                self.update_permissions_list()
        except PermissionError as e:
            print(f"Permission error: {e}")
        except Exception as e:
            print(f"Error deleting permission: {e}")

    def show(self, x: int, y: int) -> None:
        self.window.geometry(f"300x300+{x}+{y}")
        self.window.deiconify()

    def close(self) -> None:
        self.window.destroy()
