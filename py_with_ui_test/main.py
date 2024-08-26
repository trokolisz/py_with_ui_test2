import tkinter as tk
from tkinter import ttk

# Sample data for the table
data = [
    ("Alice", 25, "Engineer", ["Paris", "New York", "Tokyo"]),
    ("Bob", 30, "Doctor", ["Berlin", "Rome", "Sydney"]),
    ("Charlie", 22, "Teacher", ["London", "Beijing", "Moscow"]),
    ("David", 35, "Artist", ["Amsterdam", "Cairo", "Istanbul"]),
    ("Eve", 28, "Scientist", ["San Francisco", "Seoul", "Dubai"])
]

# Function to update the table with the search results
def search(event):
    query = search_entry.get().strip()
    if query.startswith(">"):
        try:
            age_threshold = int(query[1:])
            filtered_data = [row for row in data if row[1] > age_threshold]
        except ValueError:
            filtered_data = data  # Invalid input; show all data
    elif query.startswith("<"):
        try:
            age_threshold = int(query[1:])
            filtered_data = [row for row in data if row[1] < age_threshold]
        except ValueError:
            filtered_data = data  # Invalid input; show all data
    else:
        filtered_data = [row for row in data if query.lower() in str(row[:3]).lower()]  # Exclude places in search
    
    update_table(filtered_data)

# Function to update the table
def update_table(data):
    for row in table.get_children():
        table.delete(row)
    for index, item in enumerate(data):
        table.insert("", "end", values=item[:3], iid=index)

# Function to sort the table by column
def sort_table(col, reverse):
    sorted_data = sorted(data, key=lambda x: x[col], reverse=reverse)
    update_table(sorted_data)
    table.heading(col_name[col], command=lambda: sort_table(col, not reverse))

# Function to display places visited when a row is clicked
def on_row_select(event):
    selected_item = table.focus()
    if selected_item:
        selected_index = int(selected_item)
        selected_places = data[selected_index][3]

        if place_label_frame.winfo_ismapped():
            place_label_frame.pack_forget()
        
        place_label.config(text="\n".join(selected_places))
        place_label_frame.pack(pady=5, fill="x")

# Create the main window with a larger size
root = tk.Tk()
root.title("Data Table with Dynamic Search, Sort, and Details View")
root.geometry("500x350")

# Search bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search:")
search_label.pack(side="left")

search_entry = tk.Entry(search_frame)
search_entry.pack(side="left", padx=5)
search_entry.bind("<KeyRelease>", search)  # Trigger search on key release

# Create the table
columns = ("Name", "Age", "Occupation")
col_name = {0: "Name", 1: "Age", 2: "Occupation"}

table = ttk.Treeview(root, columns=columns, show="headings", selectmode="browse")
for col in columns:
    table.heading(col, text=col, command=lambda _col=col: sort_table(columns.index(_col), False))
    table.column(col, width=150)
table.pack(pady=10, expand=True, fill="both")
table.bind("<<TreeviewSelect>>", on_row_select)

# Frame for displaying places visited
place_label_frame = tk.Frame(root)
place_label = tk.Label(place_label_frame, text="", anchor="w", justify="left")
place_label.pack(padx=10, pady=5)

# Populate the table with initial data
update_table(data)

# Run the application
root.mainloop()
