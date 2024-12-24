import pytest
import numb3rs

def test_validate():
    assert numb3rs.validate("256.256.256.256") == False

def test_validate2():
    assert numb3rs.validate("255.255.25.256") == False

def test_validate3():
    assert numb3rs.validate("A.D.25.25") == False

def test_validate4():
    assert numb3rs.validate("0.0.0.0") == True
