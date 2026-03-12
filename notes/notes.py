from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

class NotesRecord:
    def __init__(self, notes):
        self.notes = notes
        self.idis = []

    def add_note(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        tag = input("Enter tags separated by comma: ")

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not self.notes:
            note_id = 1
        else:
            note_id = self.notes[-1]["id"] + 1

        self.notes.append({
                "id": note_id,
                "title": title,
                "description": description,
                "tags": [t.strip() for t in tag.split(",")],
                "date": date
            })
        return Fore.GREEN + f"Note with title {title} added successfully"


    def delete_note(self):
        id = int(input("Enter id for delete: "))
        if not any(note["id"] == id for note in self.notes):
            return Fore.RED + "Note not found"

        self.notes = [note for note in self.notes if note["id"] != id]

        return Fore.GREEN + f"Note with id {id} deleted successfully"

    def edit_title(self):
        note_id = int(input("Enter id for edit title: "))
        new_title = input("Enter new title for edit: ")

        for note in self.notes:
            if note["id"] == note_id:
                note["title"] = new_title
                return Fore.GREEN + f"Note title with id {note_id} edited to '{new_title}'"

        return Fore.RED + "Note not found"

    def edit_description(self):
        id = int(input("Enter id for edit description: "))
        new_description = input("Enter new description: ")

        for note in self.notes:
            if note["id"] == id:
                note["description"] = new_description
                return Fore.GREEN + f"Note description edited on {new_description} "
        return Fore.RED + "Note not found"
        
    def edit_tag(self):
        id = int(input("Enter id for edit tag: "))
        new_tags = [t.strip() for t in input("Enter new tags separated by comma: ").split(",")]
        for note in self.notes:
            if note["id"] == id:
                note["tags"] = new_tags
                return Fore.GREEN + f"Note tag edited on {new_tags}"
        return Fore.RED + "Note not found"

    def search_note(self):
        word = input("Enter word for search note: ")
        results = []

        for note in self.notes:
            if word.lower() in note["title"].lower() or \
            word.lower() in note["description"].lower() or \
            any(word.lower() in tag.lower() for tag in note["tags"]):
                results.append(note)

        if not results:
            return Fore.YELLOW + "Notes not found"

        return Fore.GREEN + f"Notes found: {results}"
    
    def search_tag(self):
        tag = input("Enter tag for search note: ")
        results = []

        for note in self.notes:
            if tag.lower() in [t.lower() for t in note["tags"]]:
                results.append(note)
        if not results:
            return Fore.RED + "This tag not found"
        return Fore.GREEN + f"Notes with tag {tag} found: {results}"
    
    def sort_by_date(self):
        sorted_notes = sorted(
            self.notes,
            key=lambda note: datetime.strptime(note["date"], "%Y-%m-%d %H:%M:%S")
        )
        result = []
        for note in sorted_notes:
            result.append(
                f"id: {note['id']}, Title: {note['title']}, Description: {note['description']}, "
                f"Tags: {note['tags']}, Date: {note['date']}"
            )
        return Fore.GREEN + "\n".join(result)
    
    def show_notes(self):
        if not self.notes:
            return "No notes available"

        result = []

        for note in self.notes:
            tags = ", ".join(note.get("tags", []))
            result.append(
                Fore.CYAN +
                f"ID: {note['id']} | Title: {note['title']} | "
                f"Description: {note['description']} | "
                f"Tags: {tags} | Date: {note['date']}"
            )

        return "\n".join(result)