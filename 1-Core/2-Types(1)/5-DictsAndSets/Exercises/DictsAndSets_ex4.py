#enter your get_names_in_common function here:

def get_names_in_common(address_book1, address_book2):
    
    names_1 = set(address_book1.keys())
    names_2 = set(address_book2.keys())
    names_in_common = names