import tkinter as tk
from tkinter import messagebox
import os


# CREATE FILE
def create_file():
    filename = file_entry.get()

    try:
        with open(filename, "w") as file:
            file.write("")

        messagebox.showinfo("Success", "File Created Successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# DELETE FILE
def delete_file():
    filename = file_entry.get()

    try:
        os.remove(filename)
        messagebox.showinfo("Success", "File Deleted Successfully")

    except FileNotFoundError:
        messagebox.showerror("Error", "File Not Found")


# RENAME FILE
def rename_file():
    old_name = old_entry.get()
    new_name = new_entry.get()

    try:
        os.rename(old_name, new_name)
        messagebox.showinfo("Success", "File Renamed Successfully")

    except FileNotFoundError:
        messagebox.showerror("Error", "File Not Found")


# WINDOW
root = tk.Tk()
root.title("GUI File Manager")
root.geometry("400x350")

title = tk.Label(root, text="FILE MANAGER", font=("Arial", 18, "bold"))
title.pack(pady=10)

# CREATE / DELETE
tk.Label(root, text="Filename").pack()

file_entry = tk.Entry(root, width=30)
file_entry.pack(pady=5)

tk.Button(
    root,
    text="Create File",
    bg="green",
    fg="white",
    width=20,
    command=create_file
).pack(pady=5)

tk.Button(
    root,
    text="Delete File",
    bg="red",
    fg="white",
    width=20,
    command=delete_file
).pack(pady=5)

# RENAME
tk.Label(root, text="Old Filename").pack(pady=5)

old_entry = tk.Entry(root, width=30)
old_entry.pack()

tk.Label(root, text="New Filename").pack(pady=5)

new_entry = tk.Entry(root, width=30)
new_entry.pack()

tk.Button(
    root,
    text="Rename File",
    bg="orange",
    fg="white",
    width=20,
    command=rename_file
).pack(pady=15)

root.mainloop()
