import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

' Tarea 3 - Interpolación - Juan Fernando De Los Ríos Guerrero '

' Ejercicio 1 - Viscosidad cinética del agua '

def coeffts(xData, yData):
    n = len(xData)
    a = yData.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (xData[i] - xData[i - j])
    return a

def evalPoly(coeff, xData, x):
    n = len(coeff)
    p = coeff[-1]
    for k in range(n - 2, -1, -1):
        p = p * (x - xData[k]) + coeff[k]
    return p

' Estos son los datos dados de la temperatura y la viscosidad del agua '

T = np.array([0, 21.1, 37.8, 54.4, 71.1, 87.8, 100])
mu_k = np.array([0.101, 1.79, 1.13, 0.696, 0.519, 0.338, 0.296])

' Ahora calculamos coeficientes del polinomio de Newton '

coeff = coeffts(T, mu_k)

' Estos son nuestros valores a interpolar ' 

T_interp = [10, 30, 60, 90]
mu_interp = [evalPoly(coeff, T, t) for t in T_interp]

' Los resltuados de la interpolación son '

print(" T (°C)   μ_k (10⁻³ m²/s)")
print("---------------------------")
for t, mu in zip(T_interp, mu_interp):
    print(f" {t:.1f}      {mu:.6f}")

' Aqui graficamos la interpolación '

T_range = np.linspace(0, 100, 100)
mu_range = [evalPoly(coeff, T, t) for t in T_range]

plt.plot(T, mu_k, "bo", label="Datos")
plt.plot(T_range, mu_range, "r", label="Interpolación de Newton")
plt.plot(T_interp, mu_interp, "go", label="Interpolación")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Viscosidad cinemática (10⁻³ m²/s)")
plt.legend()
plt.grid()
plt.show()


' Ejercicio 2 - Densidad relativa del aire '

' Estos son los datos dados de la altura y la densidad relativa del aire '

h_points = [0, 1.525, 3.050, 4.575, 6.10, 7.625, 9.150]
rho_points = [1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]


' Aqui usando scipy hacemos el polinomio de interpolación de Lagrange '

L = lagrange(h_points, rho_points)


' Aqui definimos el valor a interpolar como 10.5 '

xp = 10.5
yp = L(xp)
print(f"Polinomio de interpolación: {L}")
print(f"Para h = {xp}, la densidad relativa es ρ = {yp}")

' Graficamos '

h_range = np.linspace(0, 10, 500)
plt.plot(h_range, L(h_range), label="Interpolación de Lagrange")
plt.plot(h_points, rho_points, "o", label="Datos originales")
plt.scatter(xp, yp, color="blue", zorder=5)
plt.text(xp, yp, f"({xp:.1f}, {yp:.4f})", fontsize=12, verticalalignment="bottom")
plt.xlabel("Altura (km)")
plt.ylabel("Densidad relativa (ρ)")
plt.title("Interpolación de Lagrange para la densidad relativa del aire")
plt.legend()
plt.grid(True)
plt.show()


' Ejercicio 3 - Amplitud Vibracional '

' Usaremos el mismo método que para el ejercicio anterior'

' Estos son lso datos dados de la velocidad y la amplitud de vibración '

vel_points = [0, 400, 800, 1200, 1600]
amp_points = [0, 0.072, 0.233, 0.712, 3.400]

' Aqui usando scipy hacemos el polinomio de interpolación de Lagrange '

L = lagrange(vel_points, amp_points)

' Graficamos '

vel_range = np.linspace(0, 2500, 500) 
amp_range = L(vel_range)


plt.plot(vel_range, amp_range, label="Interpolación de Lagrange")
plt.plot(vel_points, amp_points, "o", label="Datos originales")
plt.xlabel("Velocidad (rpm)")
plt.ylabel("Amplitud (mm)")
plt.title("Interpolación de Lagrange: Amplitud vs Velocidad")
plt.legend()
plt.grid(True)
plt.show()






















