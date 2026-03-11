from help_commands import help_info
from contacts import add_contact, delete_contact, show_all, search_contact, AddressBook
from commands_enum import Command
from storage import load_data, save_data
from notes.notes import NotesRecord

ADDRESS_BOOK_DATA_FILE = "addressbook.pkl"


def main():
    print("Welcome to Personal Assistant!")
    notes = NotesRecord()

    try:
        book = load_data(ADDRESS_BOOK_DATA_FILE)
    except FileNotFoundError:
        book = AddressBook()

    while True:
        print("\nAvailable commands:", [cmd.value for cmd in Command])
        command = input("Enter a command: ").strip().lower()

        if command == Command.EXIT.value:
            save_data(book, ADDRESS_BOOK_DATA_FILE)
            print("Good bye!")
            break

        elif command == Command.HELLO.value:
            print("How can I help you?")

        elif command == Command.ADD.value:
            print(add_contact(book))

        elif command == Command.DELETE.value:
            print(delete_contact(book))

        elif command == Command.SHOW.value:
            print(show_all(book))

        elif command == Command.SEARCH.value:
            print(search_contact(book))

        elif command == Command.HELP.value:
            help_info()

        elif command == Command.ADD_NOTE.value:
            notes.add_note()

        elif command == Command.DELETE_NOTE.value:
            notes.delete_note() 

        elif command == Command.EDIT_NOTE_TITLE.value:
            notes.edit_title()   

        elif command == Command.EDIT_NOTE_DESCRIPTION.value:
            notes.edit_description()    

        elif command == Command.EDIT_NOTE_TAG.value:
            notes.edit_tag()  

        elif command == Command.SEARCH_NOTE.value:
            notes.search_note()   

        elif command == Command.SHOW_NOTES.value:
            notes.show_notes()  
            
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()