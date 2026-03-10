from collections import UserDict
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"\d{10,12}", value):
            raise ValueError("Номер телефону має містити від 10 до 12 цифр.")
        super().__init__(value)


class Email(Field):
    def __init__(self, value):
        if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", value):
            raise ValueError("Некоректний формат email.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValueError(
                "Некоректний формат дати. Використовуйте DD.MM.YYYY (наприклад, 15.05.1990)"
            )


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def set_email(self, email):
        self.email = Email(email)

    def set_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)

    def set_address(self, address):
        self.address = address

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact: {self.name.value}, Phones: {phones}, Email: {self.email}, Birthday: {self.birthday}, Address: {self.address}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False
