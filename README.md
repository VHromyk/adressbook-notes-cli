# Personal CLI Assistant (AddressBook & Notes)

A **Python console assistant** that allows you to manage **contacts** and **notes** directly from the command line.

The assistant stores data locally and allows users to organize contacts and notes, search through them, edit information, and keep data persistent between application runs.

---

# Features

## Contacts Management

The assistant allows you to manage a personal address book.

Supported functionality:

* Add contacts with:

  * name
  * phone number
  * email
  * birthday
  * address
* Search contacts by name, phone, or email
* Edit contact information
* Delete contacts
* Display contacts with upcoming birthdays
* Validate phone numbers and emails during creation or editing

---

## Notes Management

The assistant also supports working with notes.

Each note contains:

* **title**
* **text content**
* **creation date**
* **tags**

Tags help categorize notes and allow faster searching.

Supported functionality:

* Create notes
* Search notes by title or content
* Edit notes
* Delete notes
* Add and remove tags
* Search notes by tags

---

# Data Storage

All data is stored locally on the user's computer.

The assistant saves:

* contacts
* notes

Data persists between application restarts.

---

# Project Structure

```
addressbook-notes-cli
│
├── main.py
├── help_commands.py
├── requirements.txt
├── README.md
│
├── contacts
│   ├── contact.py
│   └── address_book.py
│
├── notes
│   ├── note.py
│   └── notes_book.py
│
└── storage
    └── storage.py
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/VHromyk/adressbook-notes-cli.git
cd addressbook-notes-cli
```

---

## 2. Create a virtual environment

```bash
python3 -m venv .venv
```

---

## 3. Activate the virtual environment

### Mac / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the application

```bash
python main.py
```

---

# Available Commands

## General Commands

| Command | Description             |
| ------- | ----------------------- |
| `help`  | Show available commands |
| `hello` | Greeting message        |
| `exit`  | Exit the program        |

---

# Contacts Commands

### Add contact

```
contacts add <name> <phone> <email> <birthday> <address>
```

Example:

```
contacts add John +380991234567 john@mail.com 1995-10-21 Kyiv
```

---

### Show all contacts

```
contacts show
```

---

### Find contact

```
contacts find <query>
```

Example:

```
contacts find John
contacts find gmail
```

---

### Edit contact

```
contacts edit <name> <field> <value>
```

Example:

```
contacts edit John phone +380971111111
contacts edit John email john@gmail.com
```

---

### Delete contact

```
contacts delete <name>
```

---

### Upcoming birthdays

Shows contacts with birthdays in a specified number of days.

```
contacts birthdays <days>
```

Example:

```
contacts birthdays 7
```

---

# Notes Commands

Each note contains:

* title
* text
* creation date
* tags

---

### Add note

```
notes add <title> | <text>
```

Example:

```
notes add Shopping | Buy milk, bread and eggs
```

The assistant automatically records the **creation date**.

---

### Show notes

```
notes show
```

Example output:

```
1 | Shopping
Created: 2026-03-10
Tags: home, shopping

Buy milk, bread and eggs
```

---

### Find notes

Search notes by title or text.

```
notes find <query>
```

Example:

```
notes find shopping
notes find milk
```

---

### Edit note

```
notes edit <id> <new_title> | <new_text>
```

Example:

```
notes edit 1 Shopping list | Buy milk and apples
```

---

### Delete note

```
notes delete <id>
```

---

# Tags for Notes

Tags allow categorizing notes and improving search functionality.

---

### Add tag

```
notes tag add <id> <tag>
```

Example:

```
notes tag add 1 shopping
notes tag add 1 groceries
```

---

### Remove tag

```
notes tag remove <id> <tag>
```

Example:

```
notes tag remove 1 groceries
```

---

### Find notes by tag

```
notes tag find <tag>
```

Example:

```
notes tag find shopping
```

---

### Sort notes by tag

```
notes tag sort <tag>
```

Example:

```
notes tag sort shopping
```

---

# Example CLI Session

```
Enter command: contacts add John +380991234567 john@gmail.com 1995-10-21 Kyiv
Contact added

Enter command: notes add Shopping | Buy milk and bread
Note added

Enter command: notes show

1 | Shopping
Created: 2026-03-10
Tags: shopping

Buy milk and bread

Enter command: exit
Good bye!
```

---

# Technologies

* Python 3
* CLI interface
* Virtual environments (`venv`)
* Package manager (`pip`)
* Local data storage (JSON / pickle)

---

# Future Improvements

* fuzzy command suggestions
* improved CLI navigation
* advanced search
* contact grouping
* improved tagging system
