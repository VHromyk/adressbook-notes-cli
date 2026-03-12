import re
from datetime import datetime, date


class Record:
    def __init__(self, name: str) -> None:
        self.name = name
        self.phones: list[str] = []
        self.email: str = ""
        self.birthday: str = ""
        self.address: str = ""

    def add_phone(self, phone: str) -> None:
        if not re.fullmatch(r"\+?\d{10,12}", re.sub(r"[\s\-\(\)]", "", phone)):
            raise ValueError("Invalid phone format (10-12 digits expected)")
        self.phones.append(phone)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        if old_phone not in self.phones:
            raise ValueError(f"Phone number {old_phone} not found.")

        clean_new = re.sub(r"[\s\-\(\)]", "", new_phone)
        if not re.fullmatch(r"\+?\d{10,12}", clean_new):
            raise ValueError("Invalid new phone format.")

        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def set_email(self, email: str) -> None:
        if email and not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email
        ):
            raise ValueError("Invalid email format")
        self.email = email or ""

    def set_birthday(self, birthday: str) -> None:
        if birthday:
            for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
                try:
                    datetime.strptime(birthday, fmt)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError("Invalid date format (DD.MM.YYYY or YYYY-MM-DD)")
        self.birthday = birthday or ""

    def set_address(self, address: str) -> None:
        self.address = address or ""

    def __str__(self) -> str:
        parts = [f"Name: {self.name}"]
        if self.phones:
            parts.append(f"Phone: {', '.join(self.phones)}")
        if self.email:
            parts.append(f"Email: {self.email}")
        if self.birthday:
            parts.append(f"Birthday: {self.birthday}")
        if self.address:
            parts.append(f"Address: {self.address}")
        return "\n".join(parts)


class AddressBook:
    def __init__(self) -> None:
        self.data: dict[str, Record] = {}

    def add_record(self, record: Record) -> None:
        self.data[record.name] = record

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    def get(self, name: str) -> Record | None:
        return self.data.get(name)

    # Парсинг дати
    def parse_birthday(self, birthday: str) -> date | None:
        if not birthday:
            return None

        for i in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
            try:
                return datetime.strptime(birthday, i).date()
            except ValueError:
                continue
        return None

    # Список днів народжень через N днів
    def get_upcoming_birthdays(self, days: int) -> list[tuple[str, str, int]]:
        today = date.today()
        upcoming = []

        for record in self.data.values():
            birthday = self.parse_birthday(record.birthday)
            if not birthday:
                continue

            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= days:
                upcoming.append(
                    (record.name, birthday_this_year.strftime("%d.%m.%Y"), delta_days)
                )

        upcoming.sort(key=lambda item: item[2])
        return upcoming
