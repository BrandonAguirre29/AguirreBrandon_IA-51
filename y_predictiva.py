
from values_xwyalpha import X, w

#!Esto corresponde a cuanto espero que aprenda realmente Leon Kennedy despues de los combates

def producto_punto_fila(fila):
    return sum(map(lambda X, w: X * w, fila, w))

y_hat = list(map(producto_punto_fila, X))

#print("y_hat =", y_hat)