import subprocess
import pytest

def test_fizz_buzz():
    a=[]
    for i in range(0,30):
        process_output = subprocess.run('python conditions_ex1.py', capture_output=True, input=(str(i)).encode())
        actual_output = process_output.stdout.decode('ascii')
        actual_output = actual_output.strip()
        a.append(actual_output)   
    assert 'fizz-buzz' in a[24]
    assert ('fizz' in a[26]) and (not 'buzz' in a[26])
    assert ('buzz' in a[27]) and (not 'fizz' in a[27])
    assert '29' in a[29]
#@pytest.mark.skip
def test_get_tax_rate():

    from conditions_ex2 import get_tax_rate 
    from pytest import approx
    base_rate = 20


    test_cases = [{'income':12.4, 'expected_rate':0}, 
                  {'income':12.6, 'expected_rate':20}, 
                  {'income':49.5, 'expected_rate':20}, 
                  {'income':50.5, 'expected_rate':40}] 
    
    for i, test_case in enumerate(test_cases):
        print(f"Test {i}: Using £{test_case['income']}k, Expecting {test_case['expected_rate']}")
        actual_tax_rate = get_tax_rate(test_case['income']*1000)
        assert actual_tax_rate == approx(test_case['expected_rate'])

#@pytest.mark.skip
def test_get_phone_numbers():
    process_input = 'alice\nbob\n\n'
    process_output = subprocess.run(
        ['python', 'conditions_ex3.py'], 
        capture_output = True, 
        input = process_input.encode()
        )
    actual_output = process_output.stdout.decode('ascii')
    actual_output = actual_output.strip()
    assert '01234' in actual_output
    assert '06789' in actual_output

#@pytest.mark.skip
def test_get_tax_rate_2 ():

    from conditions_ex4 import get_tax_rate 
    from pytest import approx
    base_rate = 20
    p_e_rate = 100*(12.5 * base_rate/100) / 20

    test_cases = [{'income':12.4, 'num_children':0, 'expected_rate':0}, 
                  {'income':12.4, 'num_children':2, 'expected_rate':0}, 
                  {'income':12.6, 'num_children':0, 'expected_rate':base_rate}, 
                  {'income':12.6, 'num_children':2, 'expected_rate':base_rate}, 
                  {'income':49.5, 'num_children':0, 'expected_rate':base_rate}, 
                  {'income':49.5, 'num_children':2, 'expected_rate':base_rate},
                  {'income':51.5, 'num_children':0, 'expected_rate':base_rate+20}, 
                  {'income':51.5, 'num_children':1, 'expected_rate':base_rate+20+12},
                  {'income':51.5, 'num_children':2, 'expected_rate':base_rate+20+17},
                  {'income':61.5, 'num_children':0, 'expected_rate':base_rate+20}, 
                  {'income':61.5, 'num_children':2, 'expected_rate':base_rate+20},
                  {'income':99.5, 'num_children':0, 'expected_rate':base_rate+20}, 
                  {'income':99.5, 'num_children':2, 'expected_rate':base_rate+20},
                  {'income':101.5, 'num_children':0, 'expected_rate':base_rate+20+p_e_rate}, 
                  {'income':101.5, 'num_children':2, 'expected_rate':base_rate+20+p_e_rate},
                  {'income':119.5, 'num_children':0, 'expected_rate':base_rate+20+p_e_rate}, 
                  {'income':119.5, 'num_children':2, 'expected_rate':base_rate+20+p_e_rate}, 
                  {'income':121.5, 'num_children':0, 'expected_rate':base_rate+20}, 
                  {'income':121.5, 'num_children':2, 'expected_rate':base_rate+20},
                  {'income':144.5, 'num_children':0, 'expected_rate':base_rate+20}, 
                  {'income':144.5, 'num_children':2, 'expected_rate':base_rate+20},
                  {'income':145.5, 'num_children':0, 'expected_rate':base_rate+20+5}, 
                  {'income':145.5, 'num_children':2, 'expected_rate':base_rate+20+5}]                  
    
    for i, test_case in enumerate(test_cases):
        print(f"Test {i}: Using £{test_case['income']}k with {test_case['num_children']} kids,",
                        f"Expecting {test_case['expected_rate']}")
        actual_tax_rate = get_tax_rate(test_case['income']*1000, test_case['num_children'])
        assert actual_tax_rate == approx(test_case['expected_rate'])

