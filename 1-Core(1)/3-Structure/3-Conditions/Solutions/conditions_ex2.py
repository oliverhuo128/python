# tax rate q

def get_tax_rate(income):

    if income < 12500:
        return 0
    elif income < 50000:
        return 20
    return 40
