x = [1.50, 1.60, 1.70]
y = [50, 60, 65]
n = len(x)

#Calcular sumatorias 
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i]*y[i] for i in range(n))
sum_x2 = sum(xi**2 for xi in x)

#Calcular pendiente (m)
m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)

#Calcular intercepto (b)
b = (sum_y - m*sum_x) / n


#Prediccion
altura_nueva = 1.65
peso_predicho = m*altura_nueva + b

#Leer .csv
with open("open1.csv", "r") as f:
    lineas = f.readlines()

for i in range(len(lineas)):
    partes = lineas[i].strip().split(",")

    if partes[0].strip() == "4":
        partes[2] = str(round(peso_predicho, 2))
        lineas[i] = ",".join(partes) + "\n"

with open("open1.csv", "w") as f:
    f.writelines(lineas)


#Termina de leer .csv

print("Pendiente m =", m)
print("Intercepto b =", b)
print("Peso estimado para altura", altura_nueva, "=", peso_predicho, "kg" )