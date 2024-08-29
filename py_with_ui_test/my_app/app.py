from tkinter import Tk, messagebox
from my_app.gui.windows.main_window import MainWindow
from utils.db_helper import create_table
import logging


logging.basicConfig(filename='C:/Users/danic/Desktop/temp/py_with_ui_test/my_app/logs/app.log',
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')



def main():
    try:
        create_table()
        #root = Tk()
        #root.title("Basic Tkinter App with Database")
        #app = MainWindow(root)
        #root.mainloop()
    except Exception as e:               
        logging.error(f"Error creating table: {str(e)}", exc_info=True)
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
