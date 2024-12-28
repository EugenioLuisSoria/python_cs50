from jar import Jar


def test_init():
    j = Jar(150)
    assert j.capacity_init == 150
    assert j.capacity == 150

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    j = Jar(1)
    j.deposit(1)
    assert j.size == 1

def test_withdraw():
    j = Jar(1)
    j.deposit(1)
    j.withdraw(1)
    assert j.size == 0
