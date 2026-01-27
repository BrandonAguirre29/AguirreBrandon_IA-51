from values_xwyalpha import X, w

y_hat = [sum(a * b for a, b in zip(fila, w)) for fila in X]

#zip empareja elementos posicion por posicion 
#por ejemplo en ese caso fila = [2, 5] y w = [1, 1], seria (2, 1), (5, 1)
