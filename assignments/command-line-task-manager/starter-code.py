from dataclasses import dataclass
from typing import Protocol


@dataclass
class Task:
    task_id: int
    title: str
    completed: bool = False


class TaskStore(Protocol):
    def add(self, title: str) -> Task:
        ...

    def list_all(self) -> list[Task]:
        ...

    def complete(self, task_id: int) -> Task | None:
        ...

    def delete(self, task_id: int) -> Task | None:
        ...


class InMemoryTaskStore:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title: str) -> Task:
        # TODO: Validate the title, create a Task, and store it.
        raise NotImplementedError

    def list_all(self) -> list[Task]:
        # TODO: Return tasks in ID order without exposing the dictionary.
        raise NotImplementedError

    def complete(self, task_id: int) -> Task | None:
        # TODO: Mark the matching task complete and return it.
        raise NotImplementedError

    def delete(self, task_id: int) -> Task | None:
        # TODO: Remove and return the matching task, if it exists.
        raise NotImplementedError


class Command(Protocol):
    name: str

    def execute(self) -> str:
        ...


class AddTaskCommand:
    name = "add"

    def __init__(self, store: TaskStore, title: str):
        self.store = store
        self.title = title

    def execute(self) -> str:
        task = self.store.add(self.title)
        return f"Added #{task.task_id}: {task.title}"


class ListTasksCommand:
    name = "list"

    def __init__(self, store: TaskStore):
        self.store = store

    def execute(self) -> str:
        tasks = self.store.list_all()
        if not tasks:
            return "No tasks."
        return "\n".join(
            f"[{ 'x' if task.completed else ' ' }] #{task.task_id}: {task.title}"
            for task in tasks
        )


class CompleteTaskCommand:
    name = "complete"

    def __init__(self, store: TaskStore, task_id: int):
        self.store = store
        self.task_id = task_id

    def execute(self) -> str:
        task = self.store.complete(self.task_id)
        if task is None:
            return f"Task #{self.task_id} was not found."
        return f"Completed #{task.task_id}: {task.title}"


class DeleteTaskCommand:
    name = "delete"

    def __init__(self, store: TaskStore, task_id: int):
        self.store = store
        self.task_id = task_id

    def execute(self) -> str:
        task = self.store.delete(self.task_id)
        if task is None:
            return f"Task #{self.task_id} was not found."
        return f"Deleted #{task.task_id}: {task.title}"


class ArchiveCompletedCommand:
    name = "archive"

    def __init__(self, store: TaskStore):
        self.store = store

    def execute(self) -> str:
        # TODO: Add a storage operation or composition that archives completed tasks.
        raise NotImplementedError


def build_commands(store: TaskStore) -> dict[str, type[Command]]:
    """Return command types available to the application."""
    return {
        "add": AddTaskCommand,
        "list": ListTasksCommand,
        "complete": CompleteTaskCommand,
        "delete": DeleteTaskCommand,
        "archive": ArchiveCompletedCommand,
    }


def main():
    store = InMemoryTaskStore()
    print("Task Manager")
    print("TODO: Parse user input and construct commands from build_commands().")
    print("Try completing the store and command classes first.")


if __name__ == "__main__":
    main()
