

class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        ''' Возвращает название книги. Изменение недопустимо.'''
        return self._name
    @property
    def author(self):
        ''' Возвращает автора книги. Изменение недопустимо.'''
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер для проверки

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Pages should be an integer type")
        if value <= 0:
            raise ValueError("Pages should be more than 0")
        self._pages = value


    ''' Метод repr не могут быть унаследованы, т.к. класс содержит уникальную информацию (кол-во страниц) 
    а __str__ содержит только общую информацию'''
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер для проверки

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Duration should be a float type")
        if value <= 0:
            raise ValueError("Duration should be more than 0")
        self._duration = value

    ''' Метод repr не могут быть унаследованы, т.к. класс содержит уникальную информацию (кол-во страниц) 
    а __str__ содержит только общую информацию'''
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    paperbook = PaperBook("book_1", "author_1", 100)
    audiobook = AudioBook("book_2", "author_2", 3.5)

    print(str(paperbook))      # Используется __str__ из Book
    print(repr(audiobook))     # Используется перегруженный __repr__ в AudioBook