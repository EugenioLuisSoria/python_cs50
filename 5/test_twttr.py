import pytest
from twttr import shorten


def test_upper():
    assert shorten("Caca.") == "Cc."

""" def test_number():
    with pytest.raises(AssertionError):
        shorten("5a")
 """