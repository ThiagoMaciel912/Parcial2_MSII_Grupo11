from funciones.sumamaciel import sumamaciel

def test_sumamaciel():
    assert sumamaciel(3, 5) == 8
    assert sumamaciel(-2, 2) == 0
