import pytest
import DictsAndSets_ex1
import DictsAndSets_ex2
import DictsAndSets_ex3
import DictsAndSets_ex4
import DictsAndSets_ex5
import DictsAndSets_ex6

@pytest.mark.skip
def test_cleanup_address_book():
    input_dict = {'monty python': '123456789'}
    result = DictsAndSets_ex1.cleanup_address_book(input_dict)
    assert result=={'Monty Python': '123 456789'}

@pytest.mark.skip
def test_search_address_book():
    input_dict = {'tom': '123', 'dave': '234', 'david': '345', 'daniel': '456'}
    search_string = 'dav'
    result = DictsAndSets_ex2.search_address_book(input_dict, search_string)
    assert result=={'dave': '234', 'david': '345'}    

@pytest.mark.skip
def test_count_vowels():
    input_str = "hello data engineers"
    result = DictsAndSets_ex3.count_vowels(input_str)
    assert result=={'a':2, 'e':4, 'i':1, 'o':1, 'u':0}

@pytest.mark.skip
def test_get_names_in_common():
    input_dict1 = {'tom': '123', 'dave': '234', 'david': '345', 'daniel': '456'}
    input_dict2 = {'theo': '123', 'dave': '234', 'david': '345', 'john': '456'}
    result = DictsAndSets_ex4.get_names_in_common(input_dict1, input_dict2)
    assert result == {'dave', 'david'}
@pytest.mark.skip
def test_get_numbers_in_common():
    input_dict1 = {'tom': '123', 'dave': '234', 'david': '345', 'daniel': '456'}
    input_dict2 = {'theo': '742', 'dave': '234', 'david': '948', 'john': '743'}
    result = DictsAndSets_ex5.get_numbers_in_common(input_dict1, input_dict2)
    assert result== {'234'}

@pytest.mark.skip
def test_combine_address_books():
    input_dict1 = {'tom': '123', 'dave': '234'}
    input_dict2 = {'theo': '742', 'dave': '284'}
    result = DictsAndSets_ex6.combine_address_books(input_dict1, input_dict2)
    assert result== ({'tom': '123', 'dave': '234', 'theo': '742'}, {'dave': '284'})