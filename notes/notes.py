import os

class NotesRecord:
    def __init__(self, filename="notes.txt"):
        base_dir = os.path.dirname(__file__)
        self.filename = os.path.join(base_dir, filename)
        self.notes = []
        self.load_notes()

    def load_notes(self):
        self.notes = []

        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    title = parts[0].strip()
                    description = parts[1].strip()
                    tag = parts[2].strip() if len(parts) > 2 else ""
                    self.notes.append({
                        "title": title,
                        "description": description,
                        "tag": tag
                    })

    def save_notes(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for note in self.notes:
                line = f"{note['title']} | {note['description']} | {note['tag']}\n"
                file.write(line)

    def add_title(self, title):
        self.notes.append({"title": title, "description": "", "tag": ""})
        self.save_notes()

    def add_description(self, title, description):
        for note in self.notes:
            if note["title"] == title:
                note["description"] = description
        self.save_notes()

    def add_tag(self, title, tag=""):
        for note in self.notes:
            if note["title"] == title:
                note["tag"] = tag
        self.save_notes()

    def delete_note(self, title):
        self.notes = [note for note in self.notes if note["title"] != title]
        self.save_notes()

    def edit_title(self, old_title, new_title):
        for note in self.notes:
            if note["title"] == old_title:
                note["title"] = new_title
        self.save_notes()

    def edit_description(self, title, new_description):
        for note in self.notes:
            if note["title"] == title:
                note["description"] = new_description
        self.save_notes()

    def edit_tag(self, title, new_tag):
        for note in self.notes:
            if note["title"] == title:
                note["tag"] = new_tag
        self.save_notes()

    def delete_tag(self, title):
        for note in self.notes:
            if note["title"] == title:
                note["tag"] = ""
        self.save_notes()

    def search_note(self, word):
            results = []
            for note in self.notes:
                if word.lower() in note["title"].lower() or \
                word.lower() in note["description"].lower() or \
                (note["tag"] and word.lower() in note["tag"].lower()):
                    results.append(note)
                    print(f"note_res_{results}")
            return results

    def show_notes(self):
        for note in self.notes:
            print(f"Title: {note['title']}, Description: {note['description']}, Tag: {note['tag']}")