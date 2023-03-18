#enter your cleanup_address_book function here:
# keys are the names, values are the numbers 'stored as strings' 
x = {'oliver huo': '07575218700', 'Dad': 447723351072, 'mum and sister': 447795513264, 'here is  na random number':348902574763095476354097630548764}


def cleanup_address_book(address_book):
    cleaned_address_book = {}
    for name in address_book:
        new_name = name.title()
        new_number = str(address_book[name])
        if len(new_number) > 7:
            new_new_number = new_number[0:-6] + " " + new_number[-6:]
        else:
            new_new_number = new_number
        cleaned_address_book[new_name] = new_new_number


    return cleaned_address_book    

print(cleanup_address_book(x))



