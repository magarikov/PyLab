BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book():

    def __init__(self, id_, name, pages):
        ''' Set and check parameters '''
        if not isinstance(id_, int):
            raise TypeError("Id should be integrer type")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Name should be string type")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Pages should be integrer type")
        self.pages = pages


    def __str__(self):
        str = f'Книга "{self.name}\"'
        return str

    def __repr__(self):
        str = f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
        return str

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
