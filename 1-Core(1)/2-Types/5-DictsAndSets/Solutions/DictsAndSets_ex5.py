#enter your get_numbers_in_common function here:

def get_numbers_in_common(address_book1, address_book2):
    my_set = set()
    a = list(address_book1.values())
    b = list(address_book2.values())
    for i in a:
        if i in b:
            my_set.add(f'{i}')
    return my_set