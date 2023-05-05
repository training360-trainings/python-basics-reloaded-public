import file_handler
import crud_operations

PATH = 'database/books.txt'
books = file_handler.read_file(PATH)


def list_books():
    print(books)


def find_book():
    id = input('Add meg a keresendő könyv id-ját!')
    print(crud_operations.find_item(id, books))


def update_book():
    id = input('Add meg a könyv id-ját, amit módosítani szeretnél!')
    author = input('Add meg a könyv új szerzőjét, vagy hagyd üresen a mezőt!')
    title = input('Add meg a könyv új címét, vagy hagyd üresen a mezőt!')
    book = crud_operations.find_item(id, books)
    updated_book = {
        'id': book['id'],
        'title': title if title else book['title'],
        'author': author if author else book['author']
    }
    crud_operations.update_item(id, updated_book, books)
    file_handler.write_file(PATH, books)


def create_book():
    author = input('Add meg a könyv szerzőjét!')
    title = input('Add meg a könyv címét!')
    crud_operations.create_item({'title': title, 'author': author}, books)
    file_handler.write_file(PATH, books)


def delete_book():
    id = input('Add meg a törölni kívánt könyv id-ját!')
    print(crud_operations.remove_item(id, books))
    file_handler.write_file(PATH, books)
