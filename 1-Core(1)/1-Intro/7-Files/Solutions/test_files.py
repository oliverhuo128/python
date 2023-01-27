import subprocess
import pytest

def test_read_from_file():
    process_output = subprocess.run('python files_ex1.py', capture_output=True)
    actual_output = process_output.stdout.decode('ascii')
    actual_output = actual_output.strip()
    assert 'sick' in actual_output
    assert 'bail' in actual_output
    assert 'ink' in actual_output

# Delete/comment out the following line, to test '2_append_to_file.py" 
# @pytest.mark.skip
def test_append_to_file():
    user_input = 'xyz\n'
    process_output = subprocess.run('python files_ex2.py', capture_output=True, input=user_input.encode())
    user_input = 'abc\n'
    process_output = subprocess.run('python files_ex2.py', capture_output=True, input=user_input.encode())
    actual_output = process_output.stdout.decode('ascii')
    actual_output = actual_output.strip()
    assert 'xyz' in actual_output
    assert 'abc' in actual_output


