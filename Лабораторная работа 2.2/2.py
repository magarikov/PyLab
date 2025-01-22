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

# TODO написать класс Library
class Library():

    def __init__(self, books=[]):
        '''
        initialization of book list
        [] - default value
        '''
        self.books = books

    def get_next_book_id(self):
        ''' returns book_id + 1 (to create new book)'''
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        ''' find book index'''
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
