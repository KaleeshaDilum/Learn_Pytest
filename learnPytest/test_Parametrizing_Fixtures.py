import pytest


@pytest.fixture(params=["a","b"])

def demo_fixture(request):
    print(request.param)

def test_login(demo_fixture):
    print("\ntest_login_output test_1")

# def test_logout():
#     print("test_logout")
#
# def testCalculatiomn():
#     assert 2+2==4

