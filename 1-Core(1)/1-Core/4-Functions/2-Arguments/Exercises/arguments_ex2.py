def remove_entries(address_book, begins_with):
    new_address_book = {item: address_book[item] for item in address_book if item.find(begins_with)!=0}
    return new_address_book


