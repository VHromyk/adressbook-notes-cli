from enum import Enum

class Command(Enum):
    ADD = "add contact"
    DELETE = "delete contact"
    SHOW = "show contacts"
    SEARCH = "search contact"
    HELP = "help"
    EXIT = "exit"
    HELLO = "hello"
    ADD_NOTE = "add note"
    DELETE_NOTE = "delete note"
    EDIT_NOTE_TITLE = "edit note title"
    EDIT_NOTE_DESCRIPTION = "edit note description"
    EDIT_NOTE_TAG = "edit note tag"
    SEARCH_NOTE = "search note"
    SHOW_NOTES = "show notes"
    SORTED_NOTES = "sorted notes"
