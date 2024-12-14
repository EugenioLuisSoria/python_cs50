import pytest


def f():
    raise AssertionError()
    
def f2():
    
    raise SystemExit()


def test_mytest():
    with pytest.raises(SystemExit):
        f2()

def test_mytest2():
    with pytest.raises(AssertionError):
        f()