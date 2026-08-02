# Todo List

A Django web application for managing daily tasks.

## Features

- Create, update and delete tasks
- Mark tasks as complete or undo completion
- Create, update and delete tags
- Assign multiple tags to a task
- Optional deadline for tasks
- Tasks are sorted from not completed to completed and from newest to oldest

## Pages

- Home page – displays all tasks
- Tag list – displays all tags
- Create, update and delete tasks
- Create, update and delete tags

## Technologies

- Python 3
- Django 5
- SQLite

## Installation

```bash
git clone https://github.com/o7111023-pixel/todo.git
cd todo

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## Running tests

```bash
python manage.py test
```

## Code quality

```bash
flake8 todo todo_list
```
