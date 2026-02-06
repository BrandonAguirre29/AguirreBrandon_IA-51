x = []
y = []


#Leer .csv, lo guarda como lista, cada fila es una cadena
with open("open.csv", "r") as f:
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

with open("open.csv", "w") as f: #Guardar archivo nuevo, "w" borra archivo viejo y escribe el nuevo
    f.writelines(nuevas_lineas)


print("La pendiente (m) es = ",m)
print("El intercepto (b) es = ",b)
print("Ecuación de regresión:")
print(f"y = {round(m,4)} * altura + {round(b,4)}")

