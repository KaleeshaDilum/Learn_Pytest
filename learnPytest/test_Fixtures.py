import pytest

#
# @pytest.fixture (scope="module")
# def test_setIUp():
#     print("\n Launch Browser")
#     print("\n Login")
#     print("\n Browse Product")
#     yield
#     print("\n Logout from the system")
#     print("\n Close the browser")
#
# def test_addItemsToTheCart(test_setIUp):
#     print("\nadd Items To Th eCart")
#
# def test_removeItemsFromTheCart(test_setIUp):
#     print("\n remove Items From The Cart")

@pytest.fixture
def test_CreatingUser():
    user ={"username":"test","password":"1234"}
    print("\nCreating the User")
    yield user
    print("\nDeleting the User")

def test_UserExists(test_CreatingUser):
    username = test_CreatingUser["username"]
    password = test_CreatingUser["password"]

    login_Sucessful = username == "test" and password == "1234"

    assert login_Sucessful == True