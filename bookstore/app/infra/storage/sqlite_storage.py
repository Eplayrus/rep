import sqlite3
from app.domain.book import Book
from typing import List

class SQLiteStorage:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER
                )
            ''')
            conn.commit()

    def add(self, book: Book) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(''' 
                INSERT INTO books (title, author, year)
                VALUES (?, ?, ?)
            ''', (book.title, book.author, book.year))
            conn.commit()
            return cursor.lastrowid

    def get_all(self) -> list[Book]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, title, author, year FROM books')
            rows = cursor.fetchall()
            return [Book(id=row[0], title=row[1], author=row[2], year=row[3]) for row in rows]

    def delete(self, book_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()
