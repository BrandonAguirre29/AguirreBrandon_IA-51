from values_xwyalpha import y
from nueva_prediccion import y_hat2

L = list(map(lambda par: (par[0] - par[1])**2, zip(y, y_hat2)))

print(L)

