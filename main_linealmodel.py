import values_xwyalpha as values
import y_predictiva as yp
import errorvector as evector
import errortotal as errort
from ajuste_transpuesta import grad
from ajuste_pesos import w
from nueva_prediccion import y_hat2
from nuevo_vectorerror_errortotal import e2, ErrorTotal2
from func_perdida import L

print("y_hat =", yp.y_hat)
print("error vector", evector.e)
print("ErrorTotal1 =", errort.ErrorTotal1)
print("Ajuste transpuesta es: ", grad)
print("Ajuste de pesos es: ", w)
print("La nueva prediccion es: ", y_hat2)
print("Nuevo vector error es: ", e2)
print("Nuevo Error total es: ", ErrorTotal2)

print("Funcion de perdida: ", L)