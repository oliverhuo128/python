import subprocess
import pytest


def test_get_phone_number():
    user_input = 'alice\n'
    process_output = subprocess.run('python collections_ex1.py', capture_output=True, input=user_input.encode())
    actual_output = process_output.stdout.decode('ascii')
    actual_output = actual_output.strip()
    assert '01234 567 890' in actual_output

# Delete the following line to test 'print_name_list.py'
@pytest.mark.skip
def test_print_name_list():
    process_output = subprocess.run('python collections_ex2.py', capture_output=True)
    actual_output = process_output.stdout.decode('ascii').strip()
    assert 'alice' in actual_output
    assert 'bob' in actual_output
    assert 'charlie' in actual_output


# Delete the following line to test 'print_name_dict.py' 
@pytest.mark.skip
def test_print_name_dict():
    user_input = 'bob\ndylann\n80\n'
    process_output = subprocess.run('python collections_ex3.py', capture_output=True, input=user_input.encode())
    actual_output = process_output.stdout.decode('ascii').strip()
    assert 'alice' in actual_output
    assert 'bob' in actual_output
    assert 'charlie' in actual_output
    assert '01234 567 890' in actual_output
    assert '06789 123 456' in actual_output
    assert '0987 654 321' in actual_output
    

