from values_xwyalpha import y
from nueva_prediccion import y_hat2

L = []

for i in range(3):
    L.append((y[i] - y_hat2[i])**2)

print(L)