from funciones.restacarrizo import resta_carrizo

def test_resta_carrizo():
    assert resta_carrizo(10, 5) == 5
    assert resta_carrizo(7, 2) == 5
    assert resta_carrizo(0, 4) == -4
