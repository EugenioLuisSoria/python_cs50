import pytest

def suma(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Los argumentos deben ser números"
    return a + b

def test_suma():
    # Prueba que la suma de dos números funcione correctamente
    assert suma(2, 3) == 5

    # Prueba que se lance un AssertionError cuando se pasan argumentos no numéricos
    with pytest.raises(AssertionError):
        suma("hola", 3)

if __name__ == "__main__":
    pytest.main()