import pytest
from fuel import convert, gauge


def test_comun():
     assert convert("1/5") == 20

def test_cero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_values():
    with pytest.raises(ValueError):
        convert("10/9")



def test_symbol():
    assert(gauge(20)) == "20%"

def test_E():
    assert(gauge(1)) == "E"
def test_F():
    assert(gauge(99)) == "F"

