import pytest
from datetime import date
from seasons import Born, Today

def test_born_get_valid_date(monkeypatch):
    """Test para verificar que Born.get devuelve la fecha correcta cuando la entrada es válida."""
    monkeypatch.setattr('builtins.input', lambda _: "2000-01-01")  # Simular input
    result = Born.get()
    expected = date(2000, 1, 1)  # Fecha esperada
    assert result == expected

def test_born_get_invalid_date(monkeypatch):
    """Test para verificar que Born.get finaliza con error cuando la entrada es inválida."""
    monkeypatch.setattr('builtins.input', lambda _: "2000-13-01")  # Simular entrada inválida
    with pytest.raises(SystemExit):  # Born.get debe llamar sys.exit en este caso
        Born.get()

def test_today_get():
    """Test para verificar que Today.get devuelve la fecha actual correctamente."""
    result = Today.get()
    expected = date.today()  # Fecha actual en el momento de la prueba
    assert result == expected, f"Expected {expected}, but got {result}"
