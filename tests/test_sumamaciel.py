from funciones.sumamaciel import sumamaciel

def test_sumamaciel():
    assert sumamaciel(2, 3) == 5
    assert sumamaciel(-1, 1) == 0
