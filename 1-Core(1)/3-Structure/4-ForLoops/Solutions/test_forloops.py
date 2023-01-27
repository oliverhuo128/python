import subprocess
import pytest

# @pytest.mark.skip
def test_top_left_triangle():
    import forloops_ex1
    n = 5
    output_lines = forloops_ex1.top_left_triangle(5)
    
    for i, line in enumerate(output_lines):
        print(line)
        assert line.count('*')==n-i

# @pytest.mark.skip
def test_bottom_right_triangle():
    import forloops_ex1
    n = 5
    output_lines = forloops_ex1.bottom_right_triangle(5)
    
    for i, line in enumerate(output_lines):
        print(line)
        assert line.count('*')==i+1
        assert len(line)==n
 
# @pytest.mark.skip
def test_display_shopping_lists():
    import forloops_ex2
    list_1 = ['almonds', 'walnuts', 'hazelnuts']
    list_2 = ['beer']
    list_3 = ['apples', 'oranges']

    output_lines = forloops_ex2.display_shopping_lists([list_1, list_2, list_3])
    
    [print(line) for line in output_lines]

    apples_pos = output_lines[0].find('apples')
    orange_pos = output_lines[1].find('oranges')

    assert apples_pos>0
    assert apples_pos == orange_pos
    
# @pytest.mark.skip
def test_remove_entries():
    import forloops_ex3

    address_book = {
        'alice': '1234', 
        'malice' : '2345',
        'alice springs' : '3456',
        'bob':'4567',
        'charlie': '5678'
        }
    address_book = forloops_ex3.remove_entries(address_book, 'alice')
    assert len(address_book)==3
    assert 'bob' in address_book
    assert 'malice' in address_book
    assert 'charlie' in address_book


if __name__ == '__main__':

    test_top_left_triangle()
    test_bottom_right_triangle()
    test_display_shopping_lists()