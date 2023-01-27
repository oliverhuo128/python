import subprocess
import pytest



def test_get_ten_strings():

    import a_ten_strings

    actual_output = a_ten_strings.get_ten_strings()
    expected_output = []
    assert actual_output[0]=='1'
    assert actual_output[1]=='2'
    assert actual_output[2]=='3'
    assert actual_output[7]=='3'
    assert actual_output[8]=='2'
    assert actual_output[9]=='1'


# Delete the following line to test 'b_n_strings.py'
@pytest.mark.skip
def test_get_n_strings():
    import b_n_strings
    
    actual_output = b_n_strings.get_n_strings(7)
    assert actual_output == ['1','2','3','-','3','2','1']
    actual_output = b_n_strings.get_n_strings(8)
    assert actual_output == ['1','2','3','-','-','3','2','1']

# Delete the following line to test 'b_n_strings.py'
@pytest.mark.skip
def test_get_n_strings_m_numbers():
    import b_n_strings
    actual_output = b_n_strings.get_n_strings_m_numbers(7,2)
    assert actual_output == ['1','2','-','-','-','2','1']
    actual_output = b_n_strings.get_n_strings_m_numbers(8,4)
    assert actual_output == ['1','2','3','4','4','3','2','1']

# TODO: write tests for aggreatation functions (get_mean etc) 
@pytest.mark.skip
def test_c_process_marks():
    import c_process_marks
