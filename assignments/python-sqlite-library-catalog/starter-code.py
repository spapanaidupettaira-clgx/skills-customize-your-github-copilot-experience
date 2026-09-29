import sqlite3


DATABASE_FILE = "library.db"


def create_table(connection):
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """
    )
    connection.commit()


def add_book(connection, title, author, year):
    # TODO: Insert one book using SQL parameters, then commit the change.
    pass


def list_books(connection):
    # TODO: Select all books and display their ID, title, author, and year.
    pass


def search_books(connection, search_term):
    # TODO: Search titles and authors with LIKE and return matching rows.
    pass


def update_book_year(connection, book_id, new_year):
    # TODO: Update the year for this ID, commit, and report whether it existed.
    pass


def main():
    connection = sqlite3.connect(DATABASE_FILE)
    try:
        create_table(connection)
        print("Library Catalog")
        print("TODO: Add a menu for listing, searching, adding, and updating books.")
    finally:
        connection.close()


if __name__ == "__main__":
    main()