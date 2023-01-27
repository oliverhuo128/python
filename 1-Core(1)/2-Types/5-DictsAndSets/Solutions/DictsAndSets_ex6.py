#enter your combine_address_books function here:

def combine_address_books(address_book1, address_book2):
    my_dict = {}
    my_dict2 = {}
    set1 = set(address_book1)
    for k,v in address_book1.items():
        my_dict[k] = v
    for k, v in address_book2.items():
        if k not in set1:
            my_dict[k] = v
        else:
            my_dict2[k] = v
    my_tuple = (my_dict, my_dict2)
    return my_tuple