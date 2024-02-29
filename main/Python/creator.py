import tkinter as tk
from tkinter import ttk

def add_item():
    """Copy selected item from listbox1 to listbox2."""
    selected_indices = listbox1.curselection()
    for i in selected_indices:
        listbox2.insert(tk.END, listbox1.get(i))

def delete_item():
    """Delete selected item from listbox2."""
    selected_indices = listbox2.curselection()
    for i in reversed(selected_indices):  # Reverse to avoid index shifting
        listbox2.delete(i)

def move_up():
    """Move selected item in listbox2 up by one position."""
    selected_indices = listbox2.curselection()
    for i in selected_indices:
        if i > 0:
            item = listbox2.get(i)
            listbox2.delete(i)
            listbox2.insert(i-1, item)
            listbox2.select_set(i-1)

def move_down():
    """Move selected item in listbox2 down by one position."""
    selected_indices = listbox2.curselection()
    for i in reversed(selected_indices):  # Reverse to avoid index shifting when moving down
        if i < listbox2.size() - 1:
            item = listbox2.get(i)
            listbox2.delete(i)
            listbox2.insert(i+1, item)
            listbox2.select_set(i+1)

# Create the main window
root = tk.Tk()
root.title("List Box Interaction")
root.geometry("500x300")

# Create the first list box and populate it with dictionaries as strings
listbox1 = tk.Listbox(root)
listbox1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Populate listbox1 with dictionaries represented as strings
items = [
    {"name": "Item 1", "value": 100},
    {"name": "Item 2", "value": 200},
    {"name": "Item 3", "value": 300},
    {"name": "Item 4", "value": 400},
    {"name": "Item 5", "value": 500},
]
for item in items:
    listbox1.insert(tk.END, str(item))

# Create the second list box
listbox2 = tk.Listbox(root)
listbox2.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

# Create "Add" and "Delete" buttons
add_button = ttk.Button(root, text="Add", command=add_item)
add_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

delete_button = ttk.Button(root, text="Delete", command=delete_item)
delete_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

# Adjust the positioning of "Move Up" and "Move Down" buttons for stacking with "Move Up" at the bottom
move_down_button = ttk.Button(root, text="Move Down", command=move_down)
move_down_button.grid(row=2, column=1, padx=10, pady=5, sticky="n")

move_up_button = ttk.Button(root, text="Move Up", command=move_up)
move_up_button.grid(row=1, column=1, padx=10, pady=5, sticky="n")

# Configure column weights to make the layout responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
