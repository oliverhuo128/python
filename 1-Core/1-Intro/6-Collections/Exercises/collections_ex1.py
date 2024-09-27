
phone_book = {'alice':'01234 567 890', # please don't edit these entries: used for testing 
              'bob': '06789 123 456',
              'charlie': '0987 654 321'}

name = input("name?")
if name in phone_book:
    print(phone_book[name])
else:
    print("name not in book")