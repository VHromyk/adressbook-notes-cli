from enum import Enum

class Command(Enum):
    ADD = "add contact"
    DELETE = "delete contact"
    SHOW = "show contacts"
    SEARCH = "search contact"
    HELP = "help"
    EXIT = "exit"
    HELLO = "hello"