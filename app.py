import os

FILE_NAME = "notes.txt"

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        notes = file.readlines()

    return [note.strip() for note in notes]

def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        for note in notes:
            file.write(note + "\n")

def show_notes(notes):
    if not notes:
        print("\nNo notes found.\n")
        return

    print("\nYour Notes:\n")

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")

    print()

def add_note(notes):
    note = input("Enter your note: ")
    notes.append(note)
    save_notes(notes)
    print("Note added successfully.\n")

def delete_note(notes):
    show_notes(notes)

    if not notes:
        return

    try:
        number = int(input("Enter note number to delete: "))

        if 1 <= number <= len(notes):
            removed = notes.pop(number - 1)
            save_notes(notes)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid note number.\n")

    except ValueError:
        print("Please enter a valid number.\n")

def main():
    notes = load_notes()

    while True:
        print("===== SMART NOTES APP =====")
        print("1. Show Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_notes(notes)

        elif choice == "2":
            add_note(notes)

        elif choice == "3":
            delete_note(notes)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
