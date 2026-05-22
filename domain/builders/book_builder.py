from datetime import date
from domain.book import Book

class BookBuilder:
    def __init__(self):
        self._id = 0
        self._title = ""
        self._isbn = ""
        self._description = ""
        self._editorial = ""
        self._publication_date = date.today()
        self._cover_url = ""
        self._language = "es"
        self._author = []
        self._category = []
        self._page_count = 1

    def id(self, value: int):
        self._id = value
        return self

    def title(self, value: str):
        self._title = value
        return self

    def isbn(self, value: str):
        self._isbn = value
        return self

    def description(self, value: str):
        self._description = value
        return self

    def editorial(self, value: str):
        self._editorial = value
        return self

    def publication_date(self, value: date):
        self._publication_date = value
        return self

    def cover_url(self, value: str):
        self._cover_url = value
        return self

    def language(self, value: str):
        self._language = value
        return self

    def author(self, value: list[str]):
        self._author = value
        return self

    def category(self, value: list[str]):
        self._category = value
        return self

    def page_count(self, value: int):
        self._page_count = value
        return self

    def build(self) -> Book:
        return Book(
            id=self._id,
            title=self._title,
            isbn=self._isbn,
            description=self._description,
            editorial=self._editorial,
            publication_date=self._publication_date,
            cover_url=self._cover_url,
            language=self._language,
            author=self._author,
            category=self._category,
            page_count=self._page_count,
        )