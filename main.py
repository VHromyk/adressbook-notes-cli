from help_commands import help_info
from contacts.logic import add_contact, delete_contact, show_all, search_contact


def main():
    print("Welcome to Personal Assistant!")
    while True:
        print("\nAvailable commands: [add, delete, show, search, exit, help]")
        command = input("Enter a command: ").strip().lower()

        if command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact())
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