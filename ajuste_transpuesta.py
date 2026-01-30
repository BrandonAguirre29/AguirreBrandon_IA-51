from values_xwyalpha import X
from errorvector import e

grad = list(map(lambda col: sum(map(lambda fila: X[fila][col] * e[fila], range(len(e)))), range(len(X[0]))))

