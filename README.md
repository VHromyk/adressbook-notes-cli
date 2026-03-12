## Personal CLI Assistant (AddressBook & Notes)

CLI-асистент на Python для керування контактами та нотатками з терміналу. Дані зберігаються локально у файлах `addressbook.pkl` та `notes.pkl`.

---

## Функціонал

- **Контакти**
  - додавання контакту (імʼя, телефон, email, дата народження, адреса)
  - перегляд усіх контактів
  - пошук контакту за імʼям
  - показ днів народження в найближчі N днів
- **Нотатки**
  - створення нотатки (заголовок, опис, теги)
  - видалення нотатки
  - редагування заголовка, опису, тегів
  - пошук по заголовку/опису/теґах
  - пошук нотаток за тегом
  - вивід усіх нотаток
  - сортування нотаток за датою створення
- **Сервісне**
  - команда `hello`
  - команда `exit` з збереженням даних
  - підказка схожих команд (fuzzy search)

---

## Структура проєкту

```text
adressbook-notes-cli
│
├── main.py
├── assistant.py
├── commands_enum.py
├── README.md
├── requirements.txt
│
├── contacts
│   ├── __init__.py
│   ├── address_book.py
│   └── contact.py
│
├── notes
│   ├── __init__.py
│   └── notes.py
│
└── storage
    ├── __init__.py
    ├── load_data.py
    └── save_data.py
```

---

## Встановлення

### 1. Клонування репозиторію

```bash
git clone https://github.com/VHromyk/adressbook-notes-cli.git
cd adressbook-notes-cli
```

### 2. Створення віртуального оточення

```bash
python3 -m venv .venv
```

### 3. Активація віртуального оточення

**Mac / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Встановлення залежностей

```bash
pip install -r requirements.txt
```

### 5. Запуск застосунку

```bash
python main.py
```

При запуску при першому зверненні будуть створені файли `addressbook.pkl` та `notes.pkl` (якщо їх ще немає).

---

## Формат взаємодії

Після запуску застосунок показує список доступних команд і чекає введення рядка команди:

```text
Welcome to Personal Assistant!

Available commands: ['contact add', 'contact del', 'contact show', ...]
Enter a command:
```

Команди вводяться **без аргументів** — далі застосунок задає потрібні запитання через `input`.

---

## Команди для контактів

### `contact add`

Додає новий контакт. Застосунок по черзі запитує:

- імʼя
- телефон (10–12 цифр, валідація регулярним виразом)
- email (з валідацією)
- дату народження (формати: `DD.MM.YYYY`, `YYYY-MM-DD`, `DD/MM/YYYY`)
- адресу

Приклад сесії:

```text
Enter a command: contact add
Введіть ім'я: Ivan
Введіть телефон (10-12 цифр): +380991234567
Введіть email: ivan@example.com
Введіть день народження (DD.MM.YYYY): 01.01.1990
Введіть адресу: Kyiv
Контакт 'Ivan' успішно додано!
```

### `contact del`

Видаляє контакт за імʼям.

```text
Enter a command: contact del
Введіть ім'я контакту для видалення: Ivan
Контакт 'Ivan' видалено.
```

### `contact show`

Показує всі збережені контакти у читабельному форматі.

```text
Enter a command: contact show
--- Список контактів ---
Ім'я: Ivan
Телефон: +380991234567
Email: ivan@example.com
День народження: 01.01.1990
Адреса: Kyiv
```

### `contact find`

Пошук контакту за точним імʼям.

```text
Enter a command: contact find
Введіть ім'я для пошуку: Ivan
Ім'я: Ivan
Телефон: +380991234567
...
```

### `contact bday`

Показує контакти, у яких день народження в найближчі `N` днів.

```text
Enter a command: contact bday
Введіть кількість днів: 7
Контакти з днем народження у найближчі 7 днів:
Ivan — 01.01.2026 (через 3 дн.)
```

---

## Команди для нотаток

Усі операції з нотатками працюють через обʼєкт `NotesRecord` і зберігаються у `notes.pkl`.

Формат нотатки:

- `title` — заголовок
- `description` — текст
- `tags` — список тегів
- `date` — дата створення (`YYYY-MM-DD HH:MM:SS`)

### `note add`

Додає нову нотатку.

```text
Enter a command: note add
Enter title: Shopping
Enter description: Buy milk and bread
Enter tags separated by comma: home, food
Note with title Shopping added successfully
```

### `note del`

Видаляє нотатку за заголовком.

```text
Enter a command: note del
Enter title for delete: Shopping
Note with title Shopping deleted successfully
```

### `note edit title`

Змінює заголовок нотатки.

```text
Enter a command: note edit title
Enter old title for edit: Shopping
Enter new title for edit: Shopping list
Note title Shopping edited on Shopping list
```

### `note edit description`

Змінює опис нотатки.

```text
Enter a command: note edit description
Enter title for edit description: Shopping list
Enter new description: Buy milk, bread and eggs
Note description edited on Buy milk, bread and eggs
```

### `note edit tag`

Повністю оновлює список тегів нотатки.

```text
Enter a command: note edit tag
Enter title for edit tag: Shopping list
Enter new tags separated by comma: shopping, home
Note tags edited on shopping, home
```

### `note find`

Пошук нотаток за словом у заголовку, описі або тегах.

```text
Enter a command: note find
Enter word for search note: shopping
Notes found: [{'title': 'Shopping list', 'description': 'Buy milk...', 'tags': ['shopping', 'home'], 'date': '2026-03-12 12:00:00'}]
```

### `note find tag`

Пошук нотаток за тегом.

```text
Enter a command: note find tag
Enter tag for search note: shopping
{...формат виводу списком рядків...}
```

### `show notes`

Виводить усі нотатки у форматі один запис на блок.

```text
Enter a command: show notes
Title: Shopping list, Description: Buy milk..., Tags: shopping, home, Date: 2026-03-12 12:00:00
```

### `sorted notes`

Повертає всі нотатки, відсортовані за датою створення (від найстаріших до найновіших).

```text
Enter a command: sorted notes
Title: ..., Description: ..., Tags: ..., Date: ...
```

---

## Загальні команди

### `hello`

Проста вітальна команда.

```text
Enter a command: hello
How can I help you?
```

### Невідома команда та підказка

Якщо введена команда не знайдена, асистент спробує запропонувати найбільш схожу:

```text
Enter a command: contatc add
Invalid command: 'contatc add'.
Did you mean 'contact add'? (y/n):
```

### `exit`

Зберігає `addressbook.pkl` та `notes.pkl` і завершує роботу:

```text
Enter a command: exit
Good bye!
```

---

## Технології

- Python 3
- CLI
- `venv`
- `pip`
- збереження даних через `pickle`
