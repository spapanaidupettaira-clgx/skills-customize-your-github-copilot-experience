import json
from datetime import datetime


TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from a JSON file if it exists."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, title, due_date):
    """Add a new task to the list."""
    tasks.append({
        "title": title,
        "due_date": due_date,
        "completed": False,
    })


def print_tasks(tasks):
    """Display the tasks in a simple list."""
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - {task['due_date']} [{status}]")


def main():
    tasks = load_tasks()

    # TODO: Add menu system for adding, completing, deleting, and viewing tasks.
    print("Student Planner")
    print_tasks(tasks)


if __name__ == "__main__":
    main()
