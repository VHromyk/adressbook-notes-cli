from datetime import datetime

class NotesRecord:
    def __init__(self, notes):
        self.notes = notes

    def add_note(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        tag = input("Enter tags separated by comma: ")

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.notes.append({
                "title": title,
                "description": description,
                "tags": [t.strip() for t in tag.split(",")],
                "date": date
            })
        return f"Note with title {title} added successfully"


    def delete_note(self):
        title = input("Enter title for delete: ")
        self.notes = [note for note in self.notes if note["title"] != title]
        return f"Note with title {title} deleted successfully"


    def edit_title(self):
        old_title = input("Enter old title for edit: ")
        new_title = input("Enter new title for edit: ")
        for note in self.notes:
            if note["title"] == old_title:
                note["title"] = new_title
        return f"Note title {old_title} edited on {new_title} "

    def edit_description(self):
        title = input("Enter title for edit description: ")
        new_description = input("Enter new description: ")

        for note in self.notes:
            if note["title"] == title:
                note["description"] = new_description
        return f"Note description edited on {new_description} "

    def edit_tag(self):
        title = input("Enter title for edit tag: ")
        new_tags = [t.strip() for t in input("Enter new tags separated by comma: ").split(",")]
        for note in self.notes:
            if note["title"] == title:
                note["tags"] = new_tags
        return f"Note tag edited on {new_tags}"

    def search_note(self):
        word = input("Enter word for search note: ")
        results = []

        for note in self.notes:
            if word.lower() in note["title"].lower() or \
            word.lower() in note["description"].lower() or \
            any(word.lower() in tag.lower() for tag in note["tags"]):
                results.append(note)

        if not results:
            return "Notes not found"

        return f"Notes found: {results}"
    
    def search_tag(self):
        tag = input("Enter tag for search note: ")
        results = []

        for note in self.notes:
            if tag.lower() in [t.lower() for t in note["tags"]]:
                results.append(note)
        if not results:
            return "This tag not found"
        return f"Notes with tag {tag} found: {results}"
    
    def sort_by_date(self):
        sorted_notes = sorted(
            self.notes,
            key=lambda note: datetime.strptime(note["date"], "%Y-%m-%d %H:%M:%S")
        )
        result = []
        for note in sorted_notes:
            result.append(
                f"Title: {note['title']}, Description: {note['description']}, "
                f"Tags: {note['tags']}, Date: {note['date']}"
            )
        return "\n".join(result)
    
    def show_notes(self):
        result = []

        for note in self.notes:
            tags = ", ".join(note.get("tags", []))
            result.append(
                f"Title: {note['title']}, Description: {note['description']}, "
                f"Tags: {tags}, Date: {note['date']}"
            )

        return "\n".join(result)