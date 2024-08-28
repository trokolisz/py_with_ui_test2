import tkinter as tk
from user_interface import UserInterface
from data import UserData
from exceptions import UserNotFoundError

def main() -> None:
    """Main function to start the Tkinter application."""
    try:
        root = tk.Tk()
        root.title("User Management")
        user_data = UserData()
        ui = UserInterface(root, user_data)
        root.mainloop()
    except UserNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
