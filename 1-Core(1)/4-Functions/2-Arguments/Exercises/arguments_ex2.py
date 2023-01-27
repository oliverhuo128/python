def remove_entries(address_book, begins_with):
    new_address_book = {name: phone for name, phone in address_book.items() if name.find(begins_with)!=0}
    address_book.clear()
    address_book.update(new_address_book)
    return address_book

