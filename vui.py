import speech_recognition as sr
import os

recognizer = sr.Recognizer()

print("Say command like:")
print("create test dot txt")
print("delete test dot txt")
print("rename old dot txt to new dot txt")

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)

    words = command.split()

    # CREATE
    if words[0] == "create":
        filename = words[1].replace("dot", ".")
        
        with open(filename, "w") as file:
            file.write("")

        print("File created successfully")

    # DELETE
    elif words[0] == "delete":
        filename = words[1].replace("dot", ".")

        os.remove(filename)
        print("File deleted successfully")

    # RENAME
    elif words[0] == "rename":
        old_name = words[1].replace("dot", ".")
        new_name = words[3].replace("dot", ".")

        os.rename(old_name, new_name)
        print("File renamed successfully")

    else:
        print("Invalid command")

except Exception as e:
    print("Error:", e)
