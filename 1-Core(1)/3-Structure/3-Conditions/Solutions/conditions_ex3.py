address_book = {'alice':'01234 567 890', # please don't edit these entries: used for testing 
              'bob': '06789 123 456',
              'charlie': '0987 654 321'}

while True:
    name = input('Please enter name: ')
    if name.strip()=='':
        break
    if name in address_book:
        print(address_book[name])


