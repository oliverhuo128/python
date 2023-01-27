import subprocess
import pytest
import classes_ex1


def test_try_login():
    user = classes_ex1.User('Alice', 'qwerty')
    result = user.try_login('fgfgfg')
    assert result == False
    assert user.num_failed_logins == 1
    result = user.try_login('fgfgfg')
    assert result == False
    assert user.num_failed_logins == 2
    result = user.try_login('qwerty')
    assert result == True
    assert user.num_failed_logins == 0
