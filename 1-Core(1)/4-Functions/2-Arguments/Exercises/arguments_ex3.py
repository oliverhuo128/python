def add_to_phone_book(name, number, book=None):
    if book == None:
        book = {}
    if name not in book:
        book[name] = number
    return book