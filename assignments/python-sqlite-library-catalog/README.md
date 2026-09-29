# 📘 Assignment: Python and SQLite: Library Catalog

## 🎯 Objective

Build a small library catalog that saves book records in a SQLite database. You will practice creating a table and using SQL from Python to add, display, search, and update records.

## 📝 Tasks

### 🛠️ Create the Books Database

#### Description
Use Python's built-in `sqlite3` module to create a database file and a table for books. Add sample books and display the saved records.

#### Requirements
Completed program should:

- Connect to a SQLite database file named `library.db`
- Create a `books` table with an ID, title, author, and publication year
- Add at least three sample books using SQL parameters
- Display all saved books, including each book's ID


### 🛠️ Search and Update the Catalog

#### Description
Extend the program with a menu that lets a user find books and make changes to the catalog.

#### Requirements
Completed program should:

- Let the user list all books or search titles and authors using a search term
- Let the user add a book and update a book's publication year by its ID
- Use SQL parameters for values supplied by the user
- Show a friendly message when a search has no matches or an ID does not exist
- Close the database connection when the program exits