import os

print("===== FILE MANAGER =====")
print("1. Create File")
print("2. Delete File")
print("3. Rename File")

choice = input("Enter your choice (1-3): ")

# CREATE FILE
if choice == "1":
    filename = input("Enter filename to create: ")

    try:
        with open(filename, "w") as file:
            file.write("")

        print(f"{filename} created successfully!")

    except Exception as e:
        print("Error:", e)

# DELETE FILE
elif choice == "2":
    filename = input("Enter filename to delete: ")

    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)

# RENAME FILE
elif choice == "3":
    old_name = input("Enter old filename: ")
    new_name = input("Enter new filename: ")

    try:
        os.rename(old_name, new_name)
        print(f"{old_name} renamed to {new_name}")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)

else:
    print("Invalid Choice!")
