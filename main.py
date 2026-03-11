from contacts.contact import suggest_command, execute_command
from help_commands import help_info
from contacts import add_contact, delete_contact, show_all, search_contact, AddressBook, upcoming_birthdays
from commands_enum import Command
from storage import load_data, save_data
from notes.notes import NotesRecord

ADDRESS_BOOK_DATA_FILE = "addressbook.pkl"
NOTES_FILE = "notes.pkl"

def main():
    print("Welcome to Personal Assistant!")

    try:
        book = load_data(ADDRESS_BOOK_DATA_FILE)
    except FileNotFoundError:
        book = AddressBook()

    try:
        notes = load_data(NOTES_FILE)
    except FileNotFoundError:
        notes = NotesRecord([])


    while True:

        print("\nAvailable commands:", [cmd.value for cmd in Command])
        command = input("Enter a command: ").strip().lower()

        if command == Command.EXIT.value:
            save_data(book, ADDRESS_BOOK_DATA_FILE)
            save_data(notes, NOTES_FILE)
            print("Good bye!")
            break

        if command in [cmd.value for cmd in Command]:
            execute_command(command, book)

        elif command == Command.ADD_NOTE.value:
            print(notes.add_note())

        elif command == Command.DELETE_NOTE.value:
            print(notes.delete_note())

        elif command == Command.EDIT_NOTE_TITLE.value:
            print(notes.edit_title()) 

        elif command == Command.EDIT_NOTE_DESCRIPTION.value:
            print(notes.edit_description())    

        elif command == Command.EDIT_NOTE_TAG.value:
            print(notes.edit_tag())  

        elif command == Command.SEARCH_NOTE.value:
            print(notes.search_note())

        elif command == Command.SHOW_NOTES.value:
            print(notes.show_notes())  
 
        elif command == Command.SORTED_NOTES.value:
            print(notes.sort_by_date())

        else:
            suggestion = suggest_command(command)

            if suggestion:
                print(f"Invalid command: '{command}'.")
                confirm = input(f"Did you mean '{suggestion}'? (y/n): ").strip().lower()

                if confirm == "y":
                    execute_command(suggestion, book)
                else:
                    print("Command cancelled.")

            else:
                print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()