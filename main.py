import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Definir el modelo
def modelo(t, A, B, C):
    return A * np.exp(-B * t) + C

# Datos de ejemplo (suponiendo que tienes datos experimentales)
t_data = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])  # Tiempo
T_data = np.array([60, 52, 48, 44, 39, 38, 35, 33, 32, 31, 29, 28, 27, 26, 25])  # Temperatura medida

# Ajuste de la curva
parametros, covarianza = curve_fit(modelo, t_data, T_data, p0=[35, 0.5, 25])

# Obtener los parámetros ajustados
A_opt, B_opt, C_opt = parametros
print(f"A: {A_opt}, B: {B_opt}, C: {C_opt}")

# Graficar los datos y la curva ajustada
t_fit = np.linspace(0, 70, 100)  # Puntos para la curva ajustada
T_fit = modelo(t_fit, A_opt, B_opt, C_opt)

plt.scatter(t_data, T_data, label="Datos experimentales")
plt.plot(t_fit, T_fit, label=f"Curva ajustada A: {A_opt:.2f}, B: {B_opt:.2f}, C: {C_opt:.2f}", color='red')
plt.xlabel("Tiempo (t)")
plt.ylabel("Temperatura (T)")
plt.legend()
plt.show()


