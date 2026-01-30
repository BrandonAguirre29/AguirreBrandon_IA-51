from nueva_prediccion import y_hat2
from values_xwyalpha import y

def resta_e(y, y_hat):
    return list(map(lambda y, y_hat2: y - y_hat2, y, y_hat2))

e2 = resta_e(y, y_hat2)

ErrorTotal2 = sum(map(lambda x: pow(x, 2), e2))

#print("error nuevo =", e2)
#print("ErrorTotal2 =", ErrorTotal2)
