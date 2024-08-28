import tkinter as tk
from tkinter import ttk, simpledialog
import pandas as pd

# Sample Data as a pandas DataFrame
data = pd.DataFrame([
    {"id": "123456", "name": "Alice", "username": "alice123", "enabled": True, "permissions": ["read", "write"]},
    {"id": "234567", "name": "Bob", "username": "bob234", "enabled": False, "permissions": ["read"]},
    {"id": "345678", "name": "Charlie", "username": "charlie345", "enabled": True, "permissions": ["write"]},
])

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("User Table")
        self.open_windows = []

        # Dropdown Menu for User Selection
        self.selected_user = tk.StringVar()
        self.user_dropdown = ttk.Combobox(root, textvariable=self.selected_user)
        self.user_dropdown['values'] = list(data['name'])
        self.user_dropdown.pack(pady=10)
        self.user_dropdown.bind("<<ComboboxSelected>>", self.update_table)

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

        self.update_table()

    def update_table(self, *args):
        search_value = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())

        filtered_data = data[
            data['name'].str.lower().str.contains(search_value) | 
            data['username'].str.lower().str.contains(search_value) | 
            data['id'].str.contains(search_value)
        ]

        for _, row in filtered_data.iterrows():
            self.tree.insert("", tk.END, iid=row["id"], values=(
                row["id"],
                row["name"],
                row["username"],
                "Enabled" if row["enabled"] else "Disabled",
                "View Permissions"
            ))

    def on_item_click(self, event):
        # Check if click is on the "View Permissions" cell
        item_id = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)
        if item_id and col == "#5":  # Column index of "Actions"
            # Get mouse click coordinates
            x = self.root.winfo_pointerx()
            y = self.root.winfo_pointery()
            permissions = self.get_permissions(item_id)
            self.show_permissions(x, y, item_id, permissions)

    def on_main_click(self, event):
        self.close_all_windows()

    def get_permissions(self, item_id):
        # Fetch permissions for the given item_id
        permissions = data.loc[data['id'] == item_id, 'permissions'].values[0]
        return permissions

    def show_permissions(self, x, y, item_id, permissions):
        # Create a new Toplevel window
        permissions_window = tk.Toplevel(self.root)
        permissions_window.title("Permissions")
        permissions_window.geometry(f"300x300+{x}+{y}")

        # Frame for permissions list and scrollbar
        permissions_frame = tk.Frame(permissions_window)
        permissions_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Add a canvas and scrollbar for scrolling
        canvas = tk.Canvas(permissions_frame)
        scrollbar = tk.Scrollbar(permissions_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame inside canvas to hold the listbox
        self.permissions_inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.permissions_inner_frame, anchor="nw")

        self.permissions_list = tk.Listbox(self.permissions_inner_frame, selectmode=tk.SINGLE, width=40, height=10)
        self.permissions_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.config(yscrollcommand=scrollbar.set)

        # Update permissions list
        self.update_permissions_list(item_id, permissions)

        # Update scroll region
        self.permissions_inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Frame for buttons
        buttons_frame = tk.Frame(permissions_window)
        buttons_frame.pack(pady=10, fill=tk.X)

        # Add a new permission
        def add_permission():
            new_perm = simpledialog.askstring("Add Permission", "Enter new permission:")
            if new_perm and new_perm not in permissions:
                # Update permissions in the DataFrame
                data.loc[data['id'] == item_id, 'permissions'].values[0].append(new_perm)
                # Refresh the listbox with the updated permissions
                permissions.append(new_perm)
                self.update_permissions_list(item_id, permissions)
                # Update the main table
                self.update_table()

        add_button = tk.Button(buttons_frame, text="Add Permission", command=add_permission)
        add_button.pack(side=tk.BOTTOM, pady=10)

        # Add the new window to the list of open windows
        self.open_windows.append(permissions_window)

    def update_permissions_list(self, item_id, permissions):
        # Clear the listbox before adding new items
        self.permissions_list.delete(0, tk.END)
        # Add permissions to the listbox
        for perm in permissions:
            frame = tk.Frame(self.permissions_inner_frame)
            label = tk.Label(frame, text=perm)
            label.pack(side=tk.LEFT, padx=5, pady=5)

            # Create a delete button
            delete_button = tk.Button(frame, text="X", command=lambda p=perm: self.delete_permission(item_id, p))
            delete_button.pack(side=tk.RIGHT, padx=5, pady=5)
            frame.pack(fill=tk.X)

        # Update scroll region
        self.permissions_inner_frame.update_idletasks()
        self.permissions_list.master.update_idletasks()
        self.permissions_list.master.master.update_idletasks()
        self.permissions_list.master.config(scrollregion=self.permissions_list.master.bbox("all"))

    def delete_permission(self, item_id, permission):
        # Remove the permission from the DataFrame
        permissions = data.loc[data['id'] == item_id, 'permissions'].values[0]
        if permission in permissions:
            permissions.remove(permission)
            # Refresh the permissions list in the window
            self.update_permissions_list(item_id, permissions)
        # Refresh the main table to reflect changes
        self.update_table()

    def close_all_windows(self):
        for window in self.open_windows:
            window.destroy()
        self.open_windows = []

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
