import pytest
from bank import value

def test_pay():
    assert value("Hello") == 0

def test_entire_phrase():
    assert value("Hola, que tal?") == 20
