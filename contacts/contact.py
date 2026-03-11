from commands_enum import Command
from help_commands import help_info
from .address_book import AddressBook, Record
from difflib import get_close_matches


def add_contact(book: AddressBook):
    name = input("Введіть ім'я: ").strip()
    if not name:
        return "Помилка: Ім'я не може бути порожнім."

    record = Record(name)

    phone = input("Введіть телефон (10-12 цифр): ").strip()
    try:
        if phone:
            record.add_phone(phone)
    except ValueError as e:
        return f"Помилка: {e}"

    email = input("Введіть email: ").strip()
    try:
        if email:
            record.set_email(email)
    except ValueError as e:
        return f"Помилка: {e}"

    birthday = input("Введіть день народження (DD.MM.YYYY): ").strip()
    try:
        if birthday:
            record.set_birthday(birthday)
    except ValueError as e:
        return f"Помилка: {e}"

    address = input("Введіть адресу: ").strip()
    if address:
        record.set_address(address)

    book.add_record(record)
    return f"Контакт '{name}' успішно додано!"


def delete_contact(book: AddressBook):
    name = input("Введіть ім'я контакту для видалення: ").strip()
    if book.delete(name):
        return f"Контакт '{name}' видалено."
    return "Контакт не знайдено."


def show_all(book: AddressBook):
    if not book.data:
        return "Книга контактів порожня."

    result = "\n--- Список контактів ---\n"
    result += "\n".join(str(record) for record in book.data.values())
    return result


def search_contact(book: AddressBook):
    query = input("Введіть ім'я для пошуку: ").strip()
    record = book.get(query)
    if record:
        return str(record)
    return "Контакт не знайдено."

#Інтерфейс для модуля Днів Народжень
def upcoming_birthdays(book: AddressBook):
    days_input = input("Введіть кількість днів: ").strip()

    if not days_input.isdigit():
        return "Помилка: потрібно ввести ціле невід'ємне число."

    days = int(days_input)
    upcoming = book.get_upcoming_birthdays(days)

    if not upcoming:
        return f"Немає контактів із днем народження у найближчі {days} днів."

    result = [f"Контакти з днем народження у найближчі {days} днів:"]
    for name, birthday, delta in upcoming:
        result.append(f"{name} — {birthday} (через {delta} дн.)")

    return "\n".join(result)

#Інтелектуальний помічник
def suggest_command(user_command: str) -> str | None:
    available_commands = [cmd.value for cmd in Command]
    matches = get_close_matches(user_command, available_commands, n=1, cutoff=0.5)
    return matches[0] if matches else None

#Інтелектуальний помічник - щоб не дублюувати if/else у main
def execute_command(command: str, book: AddressBook):
    if command == Command.HELLO.value:
        print("How can I help you?")

    elif command == Command.ADD.value:
        print(add_contact(book))

    elif command == Command.DELETE.value:
        print(delete_contact(book))

    elif command == Command.SHOW.value:
        print(show_all(book))

    elif command == Command.SEARCH.value:
        print(search_contact(book))

    elif command == Command.UPCOMING_BIRTHDAYS.value:
        print(upcoming_birthdays(book))

    elif command == Command.HELP.value:
        help_info()

    else:
        print("Invalid command.")