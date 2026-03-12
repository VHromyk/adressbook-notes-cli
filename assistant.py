from difflib import get_close_matches

from commands_enum import Command
from help_commands import help_info

from contacts import (
    add_contact,
    delete_contact,
    show_all,
    search_contact,
    upcoming_birthdays,
    edit_contact,
)


def suggest_command(user_command: str) -> str | None:
    available_commands = [cmd.value for cmd in Command]
    matches = get_close_matches(user_command, available_commands, n=1, cutoff=0.5)
    return matches[0] if matches else None


def execute_command(command: str, book, notes):

    if command == Command.HELLO.value:
        print("How can I help you?")

    elif command == Command.HELP.value:
        help_info()

    # Contacts
    elif command == Command.ADD.value:
        print(add_contact(book))

    elif command == Command.DELETE.value:
        print(delete_contact(book))

    elif command == Command.SHOW.value:
        print(show_all(book))

    elif command == Command.SEARCH.value:
        print(search_contact(book))

    elif command == Command.EDIT.value:
        print(edit_contact(book))    

    elif command == Command.UPCOMING_BIRTHDAYS.value:
        print(upcoming_birthdays(book))

    # Notes
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

    elif command == Command.SEARCH_NOTE_BY_TAG.value:
        print(notes.search_tag())

    else:
        print("Invalid command.")
