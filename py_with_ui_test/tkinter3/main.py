import tkinter as tk
from data import UserData
from user_interface import UserInterface

if __name__ == "__main__":
    root = tk.Tk()
    root.title("User Management")
    user_data = UserData()
    app = UserInterface(root, user_data)
    root.mainloop()
