import tkinter as tk
from tkinter import ttk, simpledialog

# Sample Data
data = [
    {"id": "123456", "name": "Alice", "username": "alice123", "enabled": True, "permissions": ["read", "write"]},
    {"id": "234567", "name": "Bob", "username": "bob234", "enabled": False, "permissions": ["read"]},
    {"id": "345678", "name": "Charlie", "username": "charlie345", "enabled": True, "permissions": ["write"]},
]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("User Table")
        self.open_windows = []

        # Search Entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=50)
        self.search_entry.pack(pady=10)
        self.search_var.trace("w", self.update_table)

        # Table
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Username", "Status", "Actions"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Actions", text="Actions")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree.bind("<ButtonRelease-1>", self.on_item_click)
        self.root.bind("<Button-1>", self.on_main_click)  # Bind click event to close all windows
        self.permissions_map = {}

        self.update_table()

    def update_table(self, *args):
        search_value = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        self.permissions_map = {}

        filtered_data = [row for row in data if search_value in row["name"].lower() or 
                         search_value in row["username"].lower() or 
                         search_value in row["id"]]

        for row in filtered_data:
            self.tree.insert("", tk.END, iid=row["id"], values=(
                row["id"],
                row["name"],
                row["username"],
                "Enabled" if row["enabled"] else "Disabled",
                "View Permissions"
            ))
            self.permissions_map[row["id"]] = row["permissions"]

    def on_item_click(self, event):
        # Check if click is on the "View Permissions" cell
        item_id = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)
        if item_id and col == "#5":  # Column index of "Actions"
            # Get mouse click coordinates
            x = self.root.winfo_pointerx()
            y = self.root.winfo_pointery()
            permissions = self.permissions_map.get(item_id, [])
            self.show_permissions(x, y, item_id, permissions)

    def on_main_click(self, event):
        self.close_all_windows()

    def show_permissions(self, x, y, item_id, permissions):
        # Create a new Toplevel window
        permissions_window = tk.Toplevel(self.root)
        permissions_window.title("Permissions")
        permissions_window.geometry(f"300x300+{x}+{y}")

        # Frame for permissions list
        permissions_frame = tk.Frame(permissions_window)
        permissions_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Add permissions content
        self.permissions_list = tk.Listbox(permissions_frame, selectmode=tk.SINGLE, width=40, height=10)
        self.permissions_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add delete button for each permission
        self.permission_buttons_frame = tk.Frame(permissions_frame)
        self.permission_buttons_frame.pack(side=tk.RIGHT, fill=tk.Y)

        for perm in permissions:
            frame = tk.Frame(self.permissions_list)
            label = tk.Label(frame, text=perm)
            label.pack(side=tk.LEFT, padx=5, pady=5)

            # Create a delete button
            delete_button = tk.Button(frame, text="X", command=lambda p=perm: self.delete_permission(item_id, p))
            delete_button.pack(side=tk.RIGHT, padx=5, pady=5)
            frame.pack(fill=tk.X)

        # Frame for buttons
        buttons_frame = tk.Frame(permissions_window)
        buttons_frame.pack(pady=10, fill=tk.X)

        # Add a new permission
        def add_permission():
            new_perm = simpledialog.askstring("Add Permission", "Enter new permission:")
            if new_perm:
                self.permissions_list.insert(tk.END, new_perm)
                permissions.append(new_perm)
                self.permissions_map[item_id] = permissions

        add_button = tk.Button(buttons_frame, text="Add Permission", command=add_permission)
        add_button.pack(side=tk.BOTTOM, pady=10)

        # Add the new window to the list of open windows
        self.open_windows.append(permissions_window)

    def delete_permission(self, item_id, permission):
        permissions = self.permissions_map.get(item_id, [])
        if permission in permissions:
            permissions.remove(permission)
            self.permissions_map[item_id] = permissions
            self.update_permissions_list(item_id, permissions)

    def update_permissions_list(self, item_id, permissions):
        # Update the listbox
        for widget in self.permissions_list.winfo_children():
            widget.destroy()
        for perm in permissions:
            frame = tk.Frame(self.permissions_list)
            label = tk.Label(frame, text=perm)
            label.pack(side=tk.LEFT, padx=5, pady=5)

            # Create a delete button
            delete_button = tk.Button(frame, text="X", command=lambda p=perm: self.delete_permission(item_id, p))
            delete_button.pack(side=tk.RIGHT, padx=5, pady=5)
            frame.pack(fill=tk.X)

    def close_all_windows(self):
        for window in self.open_windows:
            window.destroy()
        self.open_windows = []

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
