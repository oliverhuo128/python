import pytest

@pytest.mark.skip
def test_get_coffee():
    import arguments_ex1

    coffee = arguments_ex1.get_coffee(milk = 'skinny', sugar='plenty')	
    assert 'skinny' in coffee
    assert 'plenty' in coffee	
    coffee = arguments_ex1.get_coffee()	
    assert 'black' in coffee
    assert ' no ' in coffee	

# @pytest.mark.skip
def test_remove_entries():
    import arguments_ex2

    address_book = {
        'alice': '1234', 
        'malice' : '2345',
        'alice springs' : '3456',
        'bob':'4567',
        'charlie': '5678'
        }

    _ = arguments_ex2.remove_entries(address_book, 'alice')
    assert len(address_book)==3
    assert 'bob' in address_book
    assert 'malice' in address_book
    assert 'charlie' in address_book

# @pytest.mark.skip
def test_add_to_phone_book():
    import arguments_ex3
 
    my_book   = arguments_ex3.add_to_phone_book('Zach', '09876')

    arguments_ex3.add_to_phone_book('Yasmine', '08642', my_book)

    your_book = arguments_ex3.add_to_phone_book('Abel', '01234')

    assert 'Zach' in my_book
    assert 'Abel' not in my_book
    assert 'Abel' in your_book


@pytest.mark.skip
def test_process_order():
    from arguments_ex4 import process_order, salmon, duck, tofu
    output = process_order(salmon, skin='crispy', hoisin = 'plenty')
    assert output=='Getting you a Salmon, with crispy skin and plenty hoisin sauce'
    output = process_order(duck, how='rare', sauce='cherry')
    assert output=='Getting you a Duck, rare, with a cherry sauce'
    output = process_order(tofu)
    assert output=='Getting you a Tofu with plenty of soy sauce'

