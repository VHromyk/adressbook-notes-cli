from help_commands import help_info

def main():
    print("Choose the command: ['help', 'hello', 'exit']")
    while True:
        command = input("Enter a command: ")

        if command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            help_info()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
