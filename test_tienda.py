import pytest
from tienda import login_system, comprar_juego, vender_juego, mostrar_inventario
from _pytest.monkeypatch import MonkeyPatch

print("Sistema de login: \n")
def test_login_system_invalid_option(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")

    result = login_system()

    assert result == "INVALID"

def test_login_system_valid_option(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")

    result = login_system()
    assert result == "2"

def test_login_system_invalid_password(monkeypatch):
    inputs = iter(["1", "4321"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = login_system()

    assert result == "INVALID"

def test_login_system_valid_password(monkeypatch):
    inputs = iter(["1", "1234"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = login_system()
    assert result == "1"

print("Sistema Compras: ")
def test_comprar_juego_not_found(monkeypatch, capsys):
    inputs = iter(["Titulo no existente", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    comprar_juego()

    captured = capsys.readouterr()
    assert "No se encontró dicho juego en la tienda.\n" in captured.out

def test_comprar_juego_valid(monkeypatch, capsys):
    inputs = iter(["Call Of Duty Modern Warfare 3", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    comprar_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "Total a pagar: 5000" in captured.out

def test_comprar_juego_insufficient_amount(monkeypatch, capsys):
    inputs = iter(["Call Of Duty Modern Warfare 3", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    comprar_juego()

    captured = capsys.readouterr()
    assert "Faltan copias físicas para realizar la compra!\n\n" in captured.out


def test_comprar_juego_negative_amount(monkeypatch, capsys):
    inputs = iter(["Call Of Duty Modern Warfare 3", "-10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    comprar_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "ERROR" in captured.out

def test_comprar_juego_empty_tittle(monkeypatch, capsys):
    inputs = iter(["", "-10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    comprar_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "ERROR" in captured.out

def test_comprar_juego_empty_amount(monkeypatch, capsys):
    inputs = iter(["Call Of Duty Modern Warfare 3", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    comprar_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "ERROR" in captured.out
print("Sistema Ventas: ")


def test_vender_juego_empty_genre(monkeypatch, capsys):
    inputs = iter(["Call Of Duty Modern Warfare 10", "10", "", "Xbox One","15000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "ERROR" in captured.out

def test_vender_juego_empty_platform(monkeypatch, capsys):
    inputs = iter(["Call Of Duty Modern Warfare 10", "10", "Acción", "","15000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "ERROR" in captured.out

def test_vender_juego_invalid_amount(monkeypatch, capsys):

    inputs = iter(["Call Of Duty Modern Warfare 3", "-5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    assert "ERROR" in captured.out

def test_vender_juego_valid_amount(monkeypatch, capsys):

    inputs = iter(["Call Of Duty Modern Warfare 3", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "Bienvenido al menú para vender." in captured.out

def test_vender_juego_empty_title(monkeypatch, capsys):

    inputs = iter(["", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "ERROR" in captured.out

def test_vender_juego_empty_amount(monkeypatch, capsys):

    inputs = iter(["Call Of Duty Modern Warfare 3", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    print(captured)
    assert "ERROR" in captured.out
    


def test_vender_juego_invalid_price(monkeypatch, capsys):

    inputs = iter(["Call Of Duty Modern Warfare 8", "10","Accion","Xbox Series S","-15000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    assert "Valor Invalido" in captured.out

def test_vender_juego_valid_price(monkeypatch, capsys):

    inputs = iter(["Call Of Duty Modern Warfare 9", "10","Accion","Xbox Series S","5000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vender_juego()

    captured = capsys.readouterr()
    assert "Bienvenido al menú para vender." in captured.out


def test_mostrar_inventario(monkeypatch, capsys):
    mostrar_inventario()

    captured = capsys.readouterr()
    print(captured)
    assert "Inventario:" in captured.out