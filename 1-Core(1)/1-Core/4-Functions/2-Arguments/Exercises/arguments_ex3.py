def add_to_phone_book(name, number, book={}): # WRONG
    if name not in book:
        book[name] = number
    return book