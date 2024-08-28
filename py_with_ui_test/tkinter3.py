import pandas as pd
import tkinter as tk
from tkinter import ttk

df = pd.DataFrame({'A': [1, 2, 3, 1, 2, 3, 1, 2, 3,1, 2, 3, 1, 2, 3, 1, 2, 3,], 'B': [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6],
                    'C': [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9], 'D': [10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12]})


# Create a function to display the table
def display_table():
    # Create a new window
    window = tk.Toplevel(root)
    window.title("Table")

    # Create a treeview widget
    tree = ttk.Treeview(window)

    # Define the columns
    tree["columns"] = tuple(df.columns)

    # Format the columns
    for column in df.columns:
        tree.column(column, width=100)
        tree.heading(column, text=column)

    # Insert the data into the treeview
    for i, row in df.iterrows():
        tree.insert("", "end", text=i, values=tuple(row))

    # Create a scrollbar
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Pack the treeview
    tree.pack(expand=True, fill="both")

# Create the main window
root = tk.Tk()
root.title("GUI Page")

# Create a button to display the table
button = tk.Button(root, text="Show Table", command=display_table)
button.pack()



# Start the main event loop
root.mainloop()