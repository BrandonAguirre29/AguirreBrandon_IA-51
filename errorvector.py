import values_xwyalpha as values
import y_predictiva as yp

def resta_e(y, y_hat):
    return list(map(lambda y, y_hat: y - y_hat, y, y_hat))

e = resta_e(values.y, yp.y_hat)

#print("error e =", e)
