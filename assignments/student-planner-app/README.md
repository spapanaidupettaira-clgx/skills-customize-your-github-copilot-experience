# 📘 Assignment: Student Planner App

## 🎯 Objective

Build a small student planner application that helps organize homework tasks, track due dates, and display upcoming assignments in a simple, useful format.

## 📝 Tasks

### 🛠️ Create a Task Model

#### Description
Design a simple task structure that stores a name, due date, and completion status for each homework item.

#### Requirements
Completed program should:

- Represent each task using a dictionary, class, or data structure of your choice
- Include a task name, due date, and a boolean status such as `completed`
- Add at least three sample tasks to the planner
- Display all tasks in a readable list format

### 🛠️ Add Task Management Features

#### Description
Allow the user to add, mark complete, and remove tasks from the planner.

#### Requirements
Completed program should:

- Provide a way to add a new task with a title and due date
- Allow the user to mark a task as complete or incomplete
- Allow the user to delete a task from the list
- Update the displayed list after each action

### 🛠️ Save and View Upcoming Work

#### Description
Let the planner keep track of tasks over time and show which assignments are due soon.

#### Requirements
Completed program should:

- Save the planner data to a JSON file so it persists between runs
- Load saved tasks when the app starts
- Show upcoming tasks sorted by due date
- Highlight or filter tasks that are not yet completed
- Include a simple menu or command loop for interacting with the planner
