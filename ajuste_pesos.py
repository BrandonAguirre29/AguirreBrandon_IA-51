from values_xwyalpha import w, alpha
from ajuste_transpuesta import grad

w[:] = list(map(lambda par: par[0] + alpha * par[1], zip(w, grad)))

