import subprocess
def test_hello_world_func():
    output = subprocess.run('python hello_world.py', capture_output=True)
    lower_output = str(output.stdout.decode('ascii').lower())
    assert 'hello' in  lower_output
    assert 'world' in  lower_output