#enter your cleanup_address_book function here:

def cleanup_address_book(address_book):
    new_ab = {}
    for k,v in address_book.items():
        name = k.split()
        v=f'{v}'
        if len(name)==1:
            fname=name[0].capitalize()
            if len(v)>7:
                v1=v[0:-6]+' '+v[-6:]
                new_ab[fname]=v1
            else:
                new_ab[fname]=v
        if len(name)==2:
            fname=name[0].capitalize()
            lname=name[1].capitalize()
            if len(v)>7:
                v1=v[0:-6]+' '+v[-6:] 
                new_ab[fname+' '+lname]=v1
            else:
                new_ab[fname+' '+lname]=v
    return new_ab

