from abc import ABC, abstractmethod

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.domain.book import Book


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, book: Book):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get(self) -> list[Book]:
        pass


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.books = []

    def add(self, book: Book):
        self.books.append(book)
        return len(self.books) - 1

    def delete(self, id: int):
        del self.books[int(id)]

    def get(self) -> list[Book]:
        return self.books


class SQLiteDatabaseRepository(AbstractRepository):
    def __init__(self, db_url: str):
        self.db = SQLAlchemy()
        self.db.init_app(Flask(__name__))
        self.db_url = db_url

    def add(self, book: Book) -> int:
        with self.db.session as session:
            session.add(book)
            session.commit()
            return len(self.books)

    def delete(self, id: int):
        with self.db.session as session:
            book = self.books[id]
            session.delete(book)
            session.commit()

    def get(self) -> list[Book]:
        with self.db.session as session:
            return [book for book in self.books if book.id == id]