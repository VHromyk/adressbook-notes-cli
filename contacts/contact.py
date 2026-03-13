from tabulate import tabulate
from .address_book import AddressBook, Record


def add_contact(book: AddressBook):
    while True:
        name = input("Enter name (or type 'cancel' to exit): ").strip()
        if name.lower() == "cancel":
            return "Operation cancelled."
        if not name:
            print("Error: Name cannot be empty. Please try again.")
            continue
        break

    record = Record(name)

    while True:
        phone = input("Enter phone (10-12 digits, or press Enter to skip): ").strip()
        if not phone:
            break
        try:
            record.add_phone(phone)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    while True:
        email = input("Enter email (or press Enter to skip): ").strip()
        if not email:
            break
        try:
            record.set_email(email)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    while True:
        birthday = input(
            "Enter birthday (DD.MM.YYYY, or press Enter to skip): "
        ).strip()
        if not birthday:
            break
        try:
            record.set_birthday(birthday)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    address = input("Enter address (or press Enter to skip): ").strip()
    if address:
        record.set_address(address)

    book.add_record(record)
    return f"Contact '{name}' added successfully!"


def delete_contact(book: AddressBook):
    name = input("Enter name of contact to delete: ").strip()
    if book.delete(name):
        return f"Contact '{name}' deleted."
    return "Contact not found."


def show_all(book: AddressBook):
    if not book.data:
        return "Address book is empty."

    headers = ["Name", "Phones", "Email", "Birthday", "Address"]
    rows = []

    for record in book.data.values():
        rows.append(
            [
                record.name,
                ", ".join(record.phones) if record.phones else "-",
                record.email if record.email else "-",
                record.birthday if record.birthday else "-",
                record.address if record.address else "-",
            ]
        )

    return "\n" + tabulate(rows, headers=headers, tablefmt="rounded_grid")


def search_contact(book: AddressBook):
    query = input("Enter name to search: ").strip()
    record = book.get(query)
    if record:
        return str(record)
    return "Contact not found."


def edit_contact(book: AddressBook):
    name = input("Enter the name of the contact to edit: ").strip()
    record = book.get(name)

    if not record:
        return "Contact not found."

    print(f"\n--- Editing Contact: {name} ---")
    print("1. Update Phone")
    print("2. Update Email")
    print("3. Update Birthday")
    print("4. Update Address")
    print("5. Back to main menu")

    choice = input("Select an option (1-5): ").strip()

    try:
        if choice == "1":
            if record.phones:
                print(f"Current phones: {', '.join(record.phones)}")
                old_phone = input(
                    "Enter the OLD phone number to change (or leave empty to add new):"
                ).strip()
                new_phone = input("Enter the NEW phone number: ").strip()
                if old_phone:
                    record.edit_phone(old_phone, new_phone)
                else:
                    record.add_phone(new_phone)
            else:
                new_phone = input("Enter phone number to add: ").strip()
                record.add_phone(new_phone)
            return "Phone updated successfully."

        elif choice == "2":
            new_email = input("Enter new email: ").strip()
            record.set_email(new_email)
            return "Email updated successfully."

        elif choice == "3":
            new_birthday = input("Enter new birthday (DD.MM.YYYY): ").strip()
            record.set_birthday(new_birthday)
            return "Birthday updated successfully."

        elif choice == "4":
            new_address = input("Enter new address: ").strip()
            record.set_address(new_address)
            return "Address updated successfully."

        elif choice == "5":
            return "Editing cancelled."
        else:
            return "Invalid choice."

    except ValueError as e:
        return f"Error: {e}"


# Інтерфейс для модуля Днів Народжень
def upcoming_birthdays(book: AddressBook):
    days_input = input("Enter number of days: ").strip()

    if not days_input.isdigit():
        return "Error: Please enter a valid positive integer."

    days = int(days_input)
    upcoming = book.get_upcoming_birthdays(days)

    if not upcoming:
        return f"Error: There are no contacts with birthdays in the next {days} days."

    result = [f"Contacts with birthdays in the next {days} days:"]
    for name, birthday, delta in upcoming:
        result.append(f"{name} — {birthday} (in {delta} days)")

    return "\n".join(result)
