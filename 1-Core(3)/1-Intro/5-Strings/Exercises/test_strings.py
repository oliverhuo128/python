import subprocess
import pytest

def test_first_second_name():
    user_input = 'monty\npython\n'
    process_output = subprocess.run('python strings_ex1.py', capture_output=True, input=user_input.encode())
    actual_output = process_output.stdout.decode('ascii')
    actual_output = actual_output.strip()
    assert actual_output.endswith('monty python')

# Delete the following line to test '2_salary_calculator.py" 
@pytest.mark.skip
def test_base_and_bonus():
    user_input = '5000\n2000\n'
    process_output = subprocess.run('python strings_ex2.py', capture_output=True, input=user_input.encode())
    actual_output = process_output.stdout.decode('ascii')
#    print(actual_output)

    assert actual_output.strip().endswith('7000')

# Delete the following line to test '3_birthday_greeting.py" 
@pytest.mark.skip
def test_birthday_greeting():
    user_input = 'bob\ndylann\n80\n'
    process_output = subprocess.run('python strings_ex3.py', capture_output=True, input=user_input.encode())
    actual_output = process_output.stdout.decode('ascii')
    actual_output = actual_output.strip()
    assert 'Bob' in actual_output
    assert 'Dylan' in actual_output
    assert '81' in actual_output
    

