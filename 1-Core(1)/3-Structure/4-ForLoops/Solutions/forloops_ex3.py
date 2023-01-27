# def remove_entries(address_book, begins_with):
#     new_address_book = {item: address_book[item] for item in address_book if item.find(begins_with)!=0}
#     return new_address_book

def remove_entries(address_book, begins_with):
    removed_dict = {}
    for name, value in address_book.items():
        if begins_with not in name[:len(begins_with)]:
            removed_dict[name] = value

    return removed_dict