#enter your search_address_book function here:



def search_address_book(address_book, search_string):
    
    address_book_filtered = {}
    for name in address_book:
        if name.find(search_string) == 0:
            address_book_filtered[name] = address_book[name]

    return address_book_filtered

result = search_address_book({'dadav': '123', 'dave': '234', 'david': '345', 'daniel': '456'}, "dav")
print(result)








