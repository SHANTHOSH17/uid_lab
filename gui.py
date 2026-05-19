import tkinter as tk
import os

# CREATE
def create_file():
    filename = entry.get()

    with open(filename, "w") as file:
        file.write("")

    label.config(text="File Created")


# DELETE
def delete_file():
    filename = entry.get()

    os.remove(filename)

    label.config(text="File Deleted")


# RENAME
def rename_file():
    old = old_entry.get()
    new = new_entry.get()

    os.rename(old, new)

    label.config(text="File Renamed")


# WINDOW
root = tk.Tk()
root.title("File Manager")
root.geometry("300x300")

# CREATE / DELETE
tk.Label(root, text="Filename").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Create", command=create_file).pack(pady=5)

tk.Button(root, text="Delete", command=delete_file).pack(pady=5)

# RENAME
tk.Label(root, text="Old Filename").pack()

old_entry = tk.Entry(root)
old_entry.pack()

tk.Label(root, text="New Filename").pack()

new_entry = tk.Entry(root)
new_entry.pack()

tk.Button(root, text="Rename", command=rename_file).pack(pady=5)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
