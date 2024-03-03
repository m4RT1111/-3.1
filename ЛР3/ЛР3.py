class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str) -> object:
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int) -> object:
        self._pages = pages
        super().__init__(name, author)
        super().__str__()

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть численного типа')
        if pages <= 0:
            raise ValueError('Количество страниц должно быть больше нуля')
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self._duration = duration
        super().__init__(name, author)
        super().__str__()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError('Длительность должна быть типа float')
        if value <= 0:
            raise ValueError('Длительность должна быть больше нуля')
        self._duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

