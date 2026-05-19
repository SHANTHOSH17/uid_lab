import os

print("1.Create")
print("2.Delete")
print("3.Rename")

choice = input("Enter choice: ")

# CREATE
if choice == "1":
    filename = input("Enter filename: ")

    with open(filename, "w") as file:
        file.write("")

    print("File Created")

# DELETE
elif choice == "2":
    filename = input("Enter filename: ")

    os.remove(filename)

    print("File Deleted")

# RENAME
elif choice == "3":
    old = input("Old filename: ")
    new = input("New filename: ")

    os.rename(old, new)

    print("File Renamed")

else:
    print("Invalid Choice")
