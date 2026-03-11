from help_commands import help_info
from contacts.logic import add_contact, delete_contact, show_all, search_contact
from notes.notes import NotesRecord

def main():
        print("Welcome to Personal Assistant!")
        notes = NotesRecord()
        notes.show_notes()


        while True:
            print("\nAvailable commands: [add, delete, show, search, exit, help]")
            command = input("Enter a command: ").strip().lower()

            if command == "a":
                notes.add_title("Good")
                break
            elif command == "b":
                notes.add_description("Good", "commands")
            elif command == "c":
                notes.add_tag("Good", "end")
            elif command == "delete":
                print(delete_contact())
            elif command == "show":
                print(show_all())
            elif command == "search":
                print(search_contact())
            elif command == "help":
                help_info()
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()