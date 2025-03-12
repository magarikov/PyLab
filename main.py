import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Animal:
    YOUNG_AGE_THRESHOLD = 3
    HEAVY_WEIGHT_THRESHOLD = 50
    """
        Класс Animal представляет животное с определенными характеристиками:
        вид, имя, возраст и вес. Предоставляет методы для проверки, является ли
        животное молодым или тяжёлым.
        """

    def __init__(self, species: str, name: str, age: int, weight: (int, float)):
        """
        Создание и подготовка к работе объекта "Животное"
        :param species: вид животного
        :param name: имя животного
        :param age: возраст животного
        :param weight: вес животного
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: возраст и вес не могут быть отрицательными
        Примеры:
        >>> animal = Animal("Dog", "Buddy", 5, 20.5)
        >>> animal.species
        'Dog'
        >>> animal.age
        5
        >>> animal.weight
        20.5
        """
        if not isinstance(species, str):
            raise TypeError("Species should be string type")
        self.species = species
        if not isinstance(name, str):
            raise TypeError("Name should be string type")
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Age should be int type")
        if age < 0:
            raise ValueError("Age should be non-negative")
        self.age = age
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight should be int or float type")
        if weight < 0:
            raise ValueError("Weight should be non-negative")
        self.weight = weight

    def is_young(self) -> bool:
        """
        Проверяет, является ли животное молодым (младше 3 лет).
        :return: Является ли животное молодым
        Примеры:
        >>> animal = Animal("Dog", "Buddy", 2, 20.5)
        >>> animal.is_young()
        True
        >>> animal = Animal("Cat", "Whiskers", 4, 5.0)
        >>> animal.is_young()
        False
        """
        return self.age < Animal.YOUNG_AGE_THRESHOLD

    def is_heavy(self) -> bool:
        """
        Проверяет, является ли животное тяжёлым (вес больше 50 кг).
        :return: Является ли животное тяжёлым
        Примеры:
        >>> animal = Animal("Elephant", "Dumbo", 10, 120.0)
        >>> animal.is_heavy()
        True
        >>> animal = Animal("Dog", "Buddy", 5, 20.5)
        >>> animal.is_heavy()
        False
        """
        return self.weight > Animal.HEAVY_WEIGHT_THRESHOLD


class Book:
    """
        Класс Book представляет книгу с определенными характеристиками:
        название, автор, год издания и жанр. Предоставляет методы: проверка, является ли
        книга классической, получение описания книги.
        """
    def __init__(self, title: str, author: str, year: int, genre: str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param title: название книги
        :param author: автор книги
        :param year: год выпуска
        :param genre: жанр книги
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: год выпуска не может быть отрицательным
        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, "Dystopian")
        >>> book.title
        '1984'
        >>> book.author
        'George Orwell'
        >>> book.genre
        'Dystopian'
        """
        if not isinstance(title, str):
            raise TypeError("Title should be string type")
        self.title = title
        if not isinstance(author, str):
            raise TypeError("Author should be string type")
        self.author = author
        if not isinstance(year, int):
            raise TypeError("Year should be int type")
        if year < 0:
            raise ValueError("Year should be non-negative")
        self.year = year
        if not isinstance(genre, str):
            raise TypeError("Genre should be string type")
        self.genre = genre

    def is_classic(self) -> bool:
        """
        Проверяет, является ли книга классической (выпущена до 1970 года).
        :return: Является ли книга классической
        >>> book = Book("1984", "George Orwell", 1949, "Dystopian")
        >>> book.is_classic()
        True
        >>> book = Book("The Road", "Cormac McCarthy", 2006, "Post-apocalyptic")
        >>> book.is_classic()
        False
        """
        return self.year < 1970

    def get_description(self) -> str:
        """
        Возвращает описание книги.
        :return: Строка с названием книги, автором и жанром
        Пример:
        >>> book = Book("1984", "George Orwell", 1949, "Dystopian")
        >>> book.get_description()
        '1984 by George Orwell, Genre: Dystopian'
        """
        return f"{self.title} by {self.author}, Genre: {self.genre}"


class City:
    """
        Класс City представляет город с определенными характеристиками:
        Название, население и площадь. Предоставляет методы: проверяет является ли
        город мегаполисом и рассчитывает плотность населения.
        """
    def __init__(self, name: str, population: int, area: (int, float)):
        """
        Создание и подготовка к работе объекта "Город"
        :param name: название города
        :param population: население города
        :param area: площадь города
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: население и площадь не могут быть отрицательными
        Примеры:
        >>> city = City("Paris", 2148000, 105.4)
        >>> city.name
        'Paris'
        >>> city.population
        2148000
        >>> city.area
        105.4
        """
        if not isinstance(name, str):
            raise TypeError("Name should be string type")
        self.name = name
        if not isinstance(population, int):
            raise TypeError("Population should be int type")
        if population < 0:
            raise ValueError("Population should be non-negative")
        self.population = population
        if not isinstance(area, (int, float)):
            raise TypeError("Area should be int or float type")
        if area <= 0:
            raise ValueError("Area should be positive")
        self.area = area

    def population_density(self) -> float:
        """
        Рассчитывает плотность населения города.
        :return: Плотность населения
        Пример:
        >>> city = City("Paris", 2148000, 105.4)
        >>> city.population_density()
        20379.506641366224
        """
        return self.population / self.area

    def is_megacity(self) -> bool:
        """
        Проверяет, является ли город мегаполисом (население больше 10 млн).
        :return: Является ли город мегаполисом
        Примеры:
        >>> city = City("Tokyo", 37400068, 2194)
        >>> city.is_megacity()
        True
        >>> city = City("Paris", 2148000, 105.4)
        >>> city.is_megacity()
        False
        """
        return self.population > 10000000


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
