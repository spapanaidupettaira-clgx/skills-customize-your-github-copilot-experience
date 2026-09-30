# 📘 Assignment: Command-Line Task Manager Architecture

## 🎯 Objective

Build a maintainable command-line task manager by separating the task model, storage, commands, and optional extensions. You will practice designing small interfaces, composing modules, and testing software that can change without rewriting the whole program.

## 📝 Tasks

### 🛠️ Model Tasks and Isolate Storage

#### Description
Complete the `Task` model and the `TaskStore` implementation in `starter-code.py`. The application should be able to create tasks, list them, mark them complete, and remove them without the command layer knowing how tasks are stored.

#### Requirements
Completed program should:

- Represent each task with an ID, title, and completed status
- Add, list, find, complete, and delete tasks through a `TaskStore` interface
- Keep storage responsibilities inside `InMemoryTaskStore`
- Reject blank task titles with a clear `ValueError`

### 🛠️ Add Command Handlers

#### Description
Implement command classes that use the store to perform user actions. Each command should do one job and return a user-facing message rather than directly reading input or printing from the storage layer.

#### Requirements
Completed program should:

- Implement commands for adding, listing, completing, and deleting tasks
- Give every command a consistent `execute()` method
- Keep command classes independent from the concrete `InMemoryTaskStore` class
- Display helpful messages when a task ID does not exist

### 🛠️ Create an Extension Point

#### Description
Add an `ArchiveCompletedCommand` plugin that removes completed tasks. Register it in the command menu without changing the existing task model or storage interface.

#### Requirements
Completed program should:

- Implement `ArchiveCompletedCommand` as a separate command class
- Remove every completed task while leaving open tasks unchanged
- Register the new command through the command registry
- Allow another command to be added without modifying the main application loop

### 🛠️ Test the Architecture

#### Description
Write a test file using Python's built-in `unittest` module. Test both normal behavior and the boundaries between commands and storage.

#### Requirements
Completed program should:

- Include tests for adding, completing, listing, deleting, and archiving tasks
- Test at least one invalid title and one missing task ID
- Use a fresh store for each test
- Run successfully with `python3 -m unittest discover -v` from the assignment directory
