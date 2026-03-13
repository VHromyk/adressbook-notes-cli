from assistant import suggest_command, execute_command
from commands_enum import Command
from contacts import AddressBook
from notes import NotesBook


def main():
    print("Welcome to Personal Assistant!")

    book = AddressBook.load()
    notes = NotesBook.load()

    while True:
        print("\nAvailable commands:", [cmd.value for cmd in Command])
        command = input("Enter a command: ").strip().lower()

        if command == Command.EXIT.value:
            book.save()
            notes.save()
            print("Good bye!")
            break

        if command in [cmd.value for cmd in Command]:
            execute_command(command, book, notes)

        else:
            suggestion = suggest_command(command)

            if suggestion:
                print(f"Invalid command: '{command}'.")
                confirm = input(f"Did you mean '{suggestion}'? (y/n): ").strip().lower()

                if confirm == "y":
                    execute_command(suggestion, book, notes)
                else:
                    print("Command cancelled.")
            else:
                print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
