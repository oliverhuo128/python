#enter your get_names_in_common function here:

def get_names_in_common(address_book1, address_book2):
    my_set = set()
    set1 = set(address_book1)
    set2 = set(address_book2)
    for i in set1.intersection(set2):
        my_set.add(i)
    return my_set



def get_names_in_common(address_book1, address_book2):
    
    names_1 = set(address_book1.keys())
    names_2 = set(address_book2.keys())
    names_in_common = names_1.intersection(names_2)
    return names_in_common

print(get_names_in_common({}, {}))