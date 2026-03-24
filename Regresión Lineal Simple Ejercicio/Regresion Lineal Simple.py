# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =========================
# 1. Datos del problema
# =========================
# Temperaturas en grados Celsius
temperatura = np.array([10, 15, 20, 25, 30]).reshape(-1, 1)

# Ventas de cafés
ventas = np.array([300, 250, 200, 150, 100])

# =========================
# 2. Crear el modelo
# =========================
modelo = LinearRegression()

# Entrenar el modelo con los datos
modelo.fit(temperatura, ventas)

# =========================
# 3. Obtener la ecuación
# =========================
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

print("Ecuación del modelo:")
print(f"Ventas = {intercepto:.2f} + ({pendiente:.2f} * Temperatura)")

# =========================
# 4. Hacer una predicción
# =========================
nueva_temperatura = np.array([[18]])
prediccion = modelo.predict(nueva_temperatura)

print(f"\nSi la temperatura es de 18°C, se venderán aproximadamente {prediccion[0]:.0f} cafés.")

# =========================
# 5. Graficar resultados
# =========================
# Predicciones para los puntos originales
ventas_predichas = modelo.predict(temperatura)

plt.scatter(temperatura, ventas, label="Datos reales")
plt.plot(temperatura, ventas_predichas, label="Línea de regresión")

plt.title("Regresión Lineal Simple: Temperatura vs Ventas de café")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Ventas de café")
plt.legend()
plt.grid(True)
plt.show()