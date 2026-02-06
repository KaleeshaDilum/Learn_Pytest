import pytest

@pytest.fixture (scope="session" , autouse=True)
def test_setIUp():
    print("\n Launch Browser")
    print("\n Login")
    print("\n Browse Product")
    yield
    print("\n Logout from the system")
    print("\n Close the browser")