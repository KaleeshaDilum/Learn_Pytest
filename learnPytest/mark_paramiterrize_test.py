import pytest

@pytest.mark.parametrize ("a,b,final",[(2,6,8),(5,8,15),(7,1,8)])
def testAdd(a,b,final):
    assert a+b==final