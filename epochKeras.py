import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# -------- LEER CSV --------
x = []
y = []

archivo = open("dataset.csv", "r")
lineas = archivo.readlines()

for linea in lineas[1:]:   
    
    datos = linea.strip().split(",")

    horas = float(datos[0])
    resultado = int(datos[1])

    x.append(horas)
    y.append(resultado)

archivo.close()

# convertir a numpy
hora_estudio = np.array(x).reshape(-1,1)
resultado = np.array(y)

# -------- MODELO --------
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[1], activation='sigmoid')
])

# -------- COMPILAR --------
model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.1),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -------- ENTRENAMIENTO --------
print("Iniciando entrenamiento\n")

historial = model.fit(
    hora_estudio,
    resultado,
    epochs=50,
    verbose=1
)

# -------- ECUACION DEL MODELO --------
peso = model.layers[0].get_weights()[0][0][0]
bias = model.layers[0].get_weights()[1][0]

print("\n--- ECUACION DEL MODELO ---")
print(f"z = {peso:.4f} * x + {bias:.4f}")
print("Probabilidad = 1 / (1 + e^(-z))")

# -------- EJEMPLO CON LA ECUACION --------
ejemplo = 4.3
z = peso * ejemplo + bias
prob = 1 / (1 + np.exp(-z))

print("\n--- EJEMPLO USANDO LA ECUACION ---")
print(f"z = ({peso:.4f} * {ejemplo}) + {bias:.4f}")
print(f"z = {z:.4f}")
print(f"Probabilidad = {prob:.4f}")

# -------- PREDICCION CON EL MODELO --------
print("\n--- PRUEBA CON 4.3 HORAS ---")

entrada = np.array([[4.3]])
pred = model.predict(entrada)

probabilidad = pred[0][0]

clase = 1 if probabilidad >= 0.5 else 0

print(f"Horas: 4.3 -> Probabilidad: {probabilidad:.4f} -> Prediccion: {clase}")

# -------- PREDICCIONES DATASET --------
print("\n--- RESULTADOS DATASET ---")

predicciones = model.predict(hora_estudio)

for i in range(len(hora_estudio)):

    prob = predicciones[i][0]
    clase = 1 if prob >= 0.5 else 0

    print(f"Hora: {hora_estudio[i][0]} -> Probabilidad: {prob:.2f} -> Predicción: {clase}")