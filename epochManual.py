x = []
y = []

# Leer archivo CSV 
archivo = open("dataset.csv", "r")

lineas = archivo.readlines()

for linea in lineas[1:]:
    
    datos = linea.strip().split(",")
    
    horas = float(datos[0])
    resultado = int(datos[1])
    
    x.append(horas)
    y.append(resultado)

archivo.close()


# -- MODELO --

peso = 0
bias = 0
alpha = 0.1

for epoch in range(10):

    for i in range(len(x)):

        xi = x[i]
        yi = y[i]

        z = peso * xi + bias

        if z >= 0:
            prediccion = 1
        else:
            prediccion = 0

        error = yi - prediccion

        peso = peso + alpha * error * xi
        bias = bias + alpha * error

    print("Epoch:", epoch+1, "Peso:", peso, "Bias:", bias)


print("\nModelo final")
print("Peso final:", peso)
print("Bias final:", bias)
print("Ecuacion del modelo es z =", peso ," * (Hora de estudio) +", bias)


# -- PREDICCIONES --
ej = 5.2
pred = peso * ej + bias

if pred >= 0:
    pred = 1
else:
    pred = 0

print("\nPrueba -> 5.2 horas:", pred)

print("Ecuacion del modelo es z =", peso ," * 5.2 +", bias)