import pytest


@pytest.mark.skip
def test_login():
    print("\ntest_login_output 123")

@pytest.mark.regression
def test_logout():
    assert 2+2==4

@pytest.mark.sanity
def testCalculatiomn():
    assert 2+2==4

@pytest.mark.xfail
def testXfail():
    assert 2+2==4


