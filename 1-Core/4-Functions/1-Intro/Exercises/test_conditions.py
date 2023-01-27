import subprocess
import pytest

# @pytest.mark.skip
def test_refactored_logging():
    import intro_ex1
    logfile_name = ('logfile.txt')
    log_messages = ['just about to open database connection\n','just about to start data analysis\n','just about to write data to database\n']
    for i in log_messages:
        log = intro_ex1.refactored_logging(logfile_name,i)
        logfile = open(logfile_name, 'r')
        test = logfile.read()
        print(test)
        logfile.close() 
        assert test.endswith(i)

