import pytest

@pytest.fixture (params=[{"username":"Kaleesha","password":"1234"},
                         {"username":"Dilum","password":"5678"}])
def test_login(request):
    return request.param



def test_login_function(test_login):
    Username  = test_login["username"]
    Password = test_login["password"]

    print(f"\n Testing with {Username} and {Password}")