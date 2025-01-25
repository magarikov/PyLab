

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
        if not isinstance(pages, int):
            raise TypeError("Pages should be integrer type")
        if pages <= 0:
            raise TypeError("Pages should be more than 0")
        self.pages = pages


    ''' Методы str и repr не могут быть унаследованы, т.к. класс содержит уникальную информацию (кол-во страниц) '''
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Duration should be float type")
        if duration <= 0:
            raise TypeError("Duration should be more than 0")
        self.duration = duration

    ''' Методы str и repr не могут быть унаследованы, т.к. класс содержит уникальную информацию (продолжительность) '''
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

if __name__ == "__main__":

    paperbook = PaperBook("book_1", "author_1", 100)
    audiobook = AudioBook("book_2", "author_2", 3.5)

    print(paperbook.__str__())
    print(audiobook.__repr__())