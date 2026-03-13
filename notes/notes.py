import pickle
from datetime import datetime
from pathlib import Path

from colorama import Fore, init
from tabulate import tabulate

init(autoreset=True)

NOTES_DIR = Path.home() / "adressbook-notes-cli"
NOTES_FILENAME = "notes.pkl"


def _notes_data_path() -> Path:
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    return NOTES_DIR / NOTES_FILENAME


class Note:
    def __init__(
        self,
        note_id: int,
        title: str,
        description: str,
        tags: list[str],
        date: str,
    ) -> None:
        self.note_id = note_id
        self.title = title.strip()
        self.description = description.strip()
        self.tags = [t.strip() for t in tags if t.strip()]
        self.date = date

    def validate(self) -> None:
        if not self.title:
            raise ValueError("Title will not be ")

    def to_row(self) -> list[str]:
        return [
            str(self.note_id),
            self.title,
            self.description,
            ", ".join(self.tags),
            self.date,
        ]

    def __str__(self) -> str:
        tags_str = ", ".join(self.tags)
        return (
            f"ID: {self.note_id} | "
            f"Title: {self.title} | "
            f"Description: {self.description} | "
            f"Tags: {tags_str} | "
            f"Date: {self.date}"
        )

class NotesBook:
    def __init__(self, notes: list[Note] | None = None) -> None:
        self.notes: list[Note] = list(notes) if notes else []

    @classmethod
    def load(cls, path: Path | None = None) -> "NotesBook":
        filepath = path or _notes_data_path()
        if not filepath.exists():
            return cls([])
        with open(filepath, "rb") as f:
            data = pickle.load(f)
        if isinstance(data, list):
            if not data:
                return cls([])
            if isinstance(data[0], dict):
                notes = [_note_from_dict(d) for d in data]
            else:
                notes = data
            return cls(notes)
        return cls([])

    def save(self, path: Path | None = None) -> None:
        filepath = path or _notes_data_path()
        with open(filepath, "wb") as f:
            pickle.dump(self.notes, f)

    def add_note(self) -> str:
        title = input("Enter title: ").strip()
        description = input("Enter description: ").strip()
        tag = input("Enter tags separated by comma: ").strip()

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_id = 1 if not self.notes else self.notes[-1].note_id + 1
        tags_list = [t.strip() for t in tag.split(",") if t.strip()]

        note = Note(note_id, title, description, tags_list, date)
        try:
            note.validate()
        except ValueError as e:
            return Fore.RED + str(e)

        self.notes.append(note)
        return Fore.GREEN + f"Note with title {title} added successfully"

    def delete_note(self) -> str:
        try:
            note_id = int(input("Enter id for delete: ").strip())
        except ValueError:
            return Fore.RED + "Invalid id"
        for i, note in enumerate(self.notes):
            if note.note_id == note_id:
                self.notes.pop(i)
                return Fore.GREEN + f"Note with id {note_id} deleted successfully"
        return Fore.RED + "Note not found"

    def edit_title(self) -> str:
        try:
            note_id = int(input("Enter id for edit title: ").strip())
        except ValueError:
            return Fore.RED + "Invalid id"
        new_title = input("Enter new title for edit: ").strip()
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title or note.title
                return Fore.GREEN + f"Note title with id {note_id} edited to '{note.title}'"
        return Fore.RED + "Note not found"

    def edit_description(self) -> str:
        try:
            note_id = int(input("Enter id for edit description: ").strip())
        except ValueError:
            return Fore.RED + "Invalid id"
        new_description = input("Enter new description: ").strip()
        for note in self.notes:
            if note.note_id == note_id:
                note.description = new_description
                return Fore.GREEN + "Note description edited"
        return Fore.RED + "Note not found"

    def edit_tag(self) -> str:
        try:
            note_id = int(input("Enter id for edit tag: ").strip())
        except ValueError:
            return Fore.RED + "Invalid id"
        new_tags = [
            t.strip()
            for t in input("Enter new tags separated by comma: ").split(",")
            if t.strip()
        ]
        for note in self.notes:
            if note.note_id == note_id:
                note.tags = new_tags
                return Fore.GREEN + f"Note tag edited to {new_tags}"
        return Fore.RED + "Note not found"

    def search_note(self) -> str:
        word = input("Enter word for search note: ").strip().lower()
        if not word:
            return Fore.YELLOW + "Enter a search word"
        results = []
        for note in self.notes:
            if (
                word in note.title.lower()
                or word in note.description.lower()
                or any(word in t.lower() for t in note.tags)
            ):
                results.append(note)
        if not results:
            return Fore.YELLOW + "Notes not found"
        return Fore.GREEN + "Notes found:" + _notes_to_table(results)

    def search_tag(self) -> str:
        tag = input("Enter tag for search note: ").strip().lower()
        if not tag:
            return Fore.YELLOW + "Enter a tag"
        results = [n for n in self.notes if tag in [t.lower() for t in n.tags]]
        if not results:
            return Fore.RED + "This tag not found"
        return Fore.GREEN + f"Notes with tag '{tag}' found:" + _notes_to_table(results)

    def sort_by_date(self) -> str:
        if not self.notes:
            return Fore.YELLOW + "No notes available"
        try:
            sorted_notes = sorted(
                self.notes,
                key=lambda n: datetime.strptime(n.date, "%Y-%m-%d %H:%M:%S"),
            )
        except ValueError:
            sorted_notes = sorted(self.notes, key=lambda n: n.date)
        return Fore.GREEN + "Notes by date:" + _notes_to_table(sorted_notes)

    def show_notes(self) -> str:
        if not self.notes:
            return "No notes available"
        return _notes_to_table(self.notes)


def _note_from_dict(data: dict) -> Note:
    return Note(
        note_id=data["id"],
        title=data.get("title", ""),
        description=data.get("description", ""),
        tags=data.get("tags", []),
        date=data.get("date", ""),
    )


def _notes_to_table(notes: list[Note]) -> str:
    if not notes:
        return ""
    headers = ["ID", "Title", "Description", "Tags", "Date"]
    rows = [n.to_row() for n in notes]
    return "\n" + tabulate(rows, headers=headers, tablefmt="rounded_grid")

