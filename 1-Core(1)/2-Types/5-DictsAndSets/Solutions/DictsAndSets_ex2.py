#enter your search_address_book function here:

def search_address_book(address_book, search_string):
    my_dict = {}
    a = search_string.lower()
    for k,v in address_book.items():
        b = k.lower()
        if b.startswith(a):
            my_dict[k] = v
    return my_dict

def search_address_book(address_book, search_string):
    address_book_filtered = {}
    for name in address_book:
        if name.find(search_string) == 0:
            address_book_filtered[name] = address_book[name]

    return address_book_filtered

result = search_address_book({'tom': '123', 'dave': '234', 'david': '345', 'daniel': '456'}, "dav")
print(result)