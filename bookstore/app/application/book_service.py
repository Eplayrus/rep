
from app.infra.storage import mem_storage
from app.infra.storage.sqlite_storage import SQLiteStorage
from abc import ABC, abstractmethod

class BookService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, book):
        return self.storage.add(book)

    def delete(self, id):
        self.storage.delete(id)

    def get(self):
        return self.storage.get()
