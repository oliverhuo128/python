def remove_entries(address_book, begins_with):
    new_address_book = {item: address_book[item] for item in address_book if item.find(begins_with)!=0}
    address_book.clear()
    address_book.update(new_address_book)
    return address_book
	
# def remove_entries(address_book, begins_with):
#     address_book = {item: address_book[item] for item in address_book if item.find(begins_with)!=0}
#     print(address_book)
#     return address_book
	
# def remove_entries(address_book, begins_with):
#     for name, value in address_book.items():
#         if begins_with not in name[:len(begins_with)]:
#             address_book.pop(name)

#     return address_book