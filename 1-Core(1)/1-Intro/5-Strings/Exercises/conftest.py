import pytest

# You don't need to edit (or even read) this file.

# For the curious, conftest.py is a configuration file for pytest. 
# We are using it, so that we can specify the required minimum number of passed tests (eg 1!)


def pytest_addoption(parser):
    parser.addoption('--minpass', type=int, default=0, help='minimum amount of tests to pass')


def pytest_sessionstart(session):
    session.count_passed = 0


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call' and result.passed:
        item.session.count_passed += 1


def pytest_sessionfinish(session, exitstatus):
    min_passed = session.config.getoption('minpass')
    if session.count_passed < min_passed:
        session.exitstatus = 127
        reporter = session.config.pluginmanager.get_plugin('terminalreporter')
        reporter.section('Session errors', sep='-', red=True, bold=True)
        reporter.line(f'Not enough successful tests - expected at least {min_passed} to pass, passed {session.count_passed}')