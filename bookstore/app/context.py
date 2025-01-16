from flask import g

from app.application.book_service import BookService
from app.infra.storage.mem_storage import MemoryStorage
from app.infra.storage.sqlite_storage import SQLiteStorage


class Context:
    def __init__(self):
        self.book_storage = MemoryStorage()  # или SQLiteStorage("test.db")
        self.book_service = BookService(self.book_storage)


def get_context(app):
    return app.config["CONTEXT"]