from help_commands import help_info
from contacts import add_contact, delete_contact, show_all, search_contact, AddressBook
from commands_enum import Command


def main():
    print("Welcome to Personal Assistant!")

    book = AddressBook()

    while True:
        print("\nAvailable commands:", [cmd.value for cmd in Command])
        command = input("Enter a command: ").strip().lower()

        if command == Command.EXIT.value:
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

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()