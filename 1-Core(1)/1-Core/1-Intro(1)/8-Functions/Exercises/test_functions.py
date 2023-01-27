import subprocess
import pytest

import functions_ex1

@pytest.mark.skip
def test_get_full_name():
    actual_output = functions_ex1.get_full_name('Monty', 'Python')
    expected_output = "Monty Python"
    assert actual_output == expected_output


# Delete the following line to test 'get_age_from_string'
@pytest.mark.skip
def test_get_age_from_valid_string():
    user_inputs = ['42', '43']
    expected_outputs = [42,43]
    for user_input,expected_output in zip(user_inputs, expected_outputs):
        actual_output = functions_ex1.get_age_from_string(user_input)
        assert actual_output == expected_output

# Delete the following line to test 'get_age_from_string'
@pytest.mark.skip
def test_get_age_from_invalid_string():
    user_inputs = ['forty', '-40']
    expected_outputs = ['not known','not known']
    for user_input,expected_output in zip(user_inputs, expected_outputs):
        actual_output = functions_ex1.get_age_from_string(user_input)
        assert actual_output == expected_output#

# Delete the following line to test 'ask_user_for_age'
@pytest.mark.skip
def test_ask_user_for_age():
    user_input = 'ten\ntwenty\n30\n'
    process_output = subprocess.run('python functions_ex2.py', capture_output=True, input=user_input.encode())
    actual_output = process_output.stdout.decode('ascii')
    print(actual_output)
    assert actual_output.strip().endswith('30')




