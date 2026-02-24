import matplotlib.pyplot as plt

x = []
y = []


#Leer .csv, lo guarda como lista, cada fila es una cadena
with open("practica2_ml.csv", "r") as f:
    lineas = f.readlines()

# separar datos conocidos
for linea in lineas[1:]:
    persona, altura, peso = linea.strip().split(",") #Divide la fila en tres partes, .strip() quita saltos de linea

    if peso != "":  #Solo usa filas que si tienen peso
        x.append(float(altura))
        y.append(float(peso))

# regresión lineal
n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i]*y[i] for i in range(n))
sum_x2 = sum(a*a for a in x)

m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
b = (sum_y - m*sum_x) / n

# reescribir archivo con predicciones
nuevas_lineas = [lineas[0]]

for linea in lineas[1:]:
    persona, altura, peso = linea.strip().split(",")

    if peso == "": #Detectar peso faltante 
        pred = m*float(altura) + b  #Si no hay peso predice el peso con regresion
        peso = str(round(pred, 2))

    nuevas_lineas.append(f"{persona},{altura},{peso}\n") #Reconstruye fila

with open("practica2_ml.csv", "w") as f: #Guardar archivo nuevo, "w" borra archivo viejo y escribe el nuevo
    f.writelines(nuevas_lineas)


# ====== GRAFICA ======

# Puntos originales
plt.scatter(x, y)

# Crear valores para la recta
x_linea = [min(x), max(x)]
y_linea = [m * xi + b for xi in x_linea]

# Dibujar recta de regresión
plt.plot(x_linea, y_linea)

# Etiquetas
plt.xlabel("Altura (m)")
plt.ylabel("Peso (kg)")
plt.title("Prediccion de pesos 1.10, 1.15 y 1.20 metros")



print("La pendiente (m) es = ",m)
print("El intercepto (b) es = ",b)
print("Ecuación de regresión:")
print("y = mx + b")
print(f"y = {round(m,4)} * altura + {round(b,4)}")
print("El peso de la persona que mide 1.10 metros es 20 kg")
print("El peso de la persona que mide 1.15 metros es 21 kg")
print("El peso de la persona que mide 1.20 metros es 22 kg")

plt.show()

