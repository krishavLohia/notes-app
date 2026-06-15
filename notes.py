# ALL FUNCTIONS
notes = []
def saveNotes():
    with open("notes.txt","w") as file:
        for note in notes:
            file.write(note + "\n")
def addNote():
    note = input("Enter your note:")
    if note.strip() == "":
        print("Your note was empty! It was not added.")
    else:
        notes.append(note)
        saveNotes()
def loadNotes():
    global notes
    try:
        with open("notes.txt", "r") as file:
            for line in file:
                notes.append(line.strip())
        print("Previous data imported.\n")
    except FileNotFoundError:
        notes = []
def getNotes():
    print("Your notes:")
    if len(notes) == 0:
        print("No notes found.")
    for i in range(len(notes)):
        print(f"[{i}]",notes[i])
    print("Total number of notes:",len(notes))
def clearNotes():
    confirm = input("Are you sure you want to delete all notes?(y/n):")
    if confirm=="y":
        notes.clear()
    else:
        print("Operation cancelled.")
    saveNotes()
def deleteNote():
    for i in range(len(notes)):
        print(f"[{i}]",notes[i])
    index = int(input("Give the index of the note you want to delete: "))
    if index>=len(notes) or index<0:
        print("Invalid index given, operation cancelled.")
    else:
        del notes[index]
        print("Note deleted.")
    saveNotes()

# TO LOAD NOTES INITIALLY AT THE START OF THE PROGRAM
loadNotes()

# MAIN MENU LOOP
while True:
    print()
    print("--MID NOTES APP--")
    print("1. Add note")
    print("2. View notes")
    print("3. Clear notes")
    print("4. Delete note")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        addNote()
    elif choice == "2":
        getNotes()
    elif choice == "3":
        clearNotes()
    elif choice == "4":
        deleteNote()
    elif choice == "5":
        break
    else:
        print("Invalid choice, please choose from the given options.")
