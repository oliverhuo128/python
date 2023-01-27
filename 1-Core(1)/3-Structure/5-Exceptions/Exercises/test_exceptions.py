import exceptions_exercises

# Same test as used in PY01.01.Intro.08.Functions:
def test_get_age_from_valid_string():
    user_inputs = ['42', '43']
    expected_outputs = [42,43]
    for user_input,expected_output in zip(user_inputs, expected_outputs):
        actual_output = exceptions_exercises.get_age_from_string(user_input)
        assert actual_output == expected_output

# Same test as used in PY01.01.Intro.08.Functions:
def test_get_age_from_invalid_string():
    user_inputs = ['forty', '-40']
    expected_outputs = ['not known','not known']
    for user_input,expected_output in zip(user_inputs, expected_outputs):
        actual_output = exceptions_exercises.get_age_from_string(user_input)
        assert actual_output == expected_output


import pytest

# Delete the following line to test 'get_age_from_string_v2.py" 
# @pytest.mark.skip
def test_get_age_from_string_v2():
    user_inputs = ['forty-two', '-1']
    for user_input in user_inputs:
        try:
            exceptions_exercises.get_age_from_string_v2(user_input)
            assert False
        except Exception as e:
            assert 'invalid' in str(e).lower()

# Delete the following line to test 'get_age_from_string_v3.py" 
# @pytest.mark.skip
def test_get_age_from_string_v3():
    user_inputs = ['forty-two', '-1', '151']
    expected_exceptions = [TypeError, ValueError, ValueError]
    for user_input, expected_exception in zip(user_inputs, expected_exceptions):
        try:
            exceptions_exercises.get_age_from_string_v3(user_input)
            assert False
        except Exception as e:
            assert type(e) is expected_exception