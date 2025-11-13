from funciones.multiplicacioncaceres import multiplicacioncaceres
def test_multiplicar():
 assert multiplicacioncaceres(3, 4) == 12
 assert multiplicacioncaceres(-2, 5) == -10