from sqlite3 import connect, IntegrityError


def create_connection():
    conn = connect("library.db")
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    );
    """
    )
    conn.commit()
    conn.close()


def add_book(title, author, year):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?);",
            (title, author, year)
        )
        conn.commit()
    except IntegrityError as e:
        print(f"Error adding book: {e}")
    finally:
        conn.close()


def get_all_books():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    conn.close()
    return books


def update_book(book_id, title, author, year):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?;",
        (title, author, year, book_id)
    )
    conn.commit()
    conn.close()


def delete_book(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?;", (book_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    add_book("Kolobok", "Afanasiev", 1960)
    add_book("War and Peace", "Leo Tolstoy", 1869)

    print("Все книги:")
    books = get_all_books()
    for book in books:
        print(book)

    update_book(1, "Kolobok - Updated", "Afanasiev", 1961)
    print("Обновленная книга:")
    print(get_all_books()[0])

    delete_book(2)
    print("Книги после удаления:")
    print(get_all_books())
