import numpy as np
import matplotlib.pyplot as plt
from math import *
import math
from cmath import sin, sinh, exp




' Examen 1 - Juan Fernando De Los Ríos Guerrero '


' Ejercicio 4 - Calor específico del aluminio'

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


T = np.array([-250.0, -200.0, -100.0, 0.0, 100.0, 300.0])
C = np.array([0.0163, 0.318, 0.699, 0.870, 0.941, 1.04])

coeff = coeffts(T, C)
x = np.arange(0.0, 8.5, 0.5)


plt.plot(T, C, "r", label="Interpolación Newton")
plt.plot(T, C, "o", label="Datos")
plt.legend()
plt.grid()
plt.show()
print("  x    yExacta        yInt       Error(%)")
print("------------------------------------------")
for i in range(len(x)):
    y = evalPoly(coeff, T, x[i])
    yExacta = 4.8 * cos(pi * x[i] / 20)
    Error = abs(((yExacta - y) / yExacta) * 100)
    print(" %.1f  %.8f   %.8f    %.8f" % (x[i], yExacta, y, Error))




' Ejercicio 3 - Un viajero en Europa'


' Este es el algoritmo de eliminación de Gauss'

' 2x+3y+2z = 27 (Gastos en hospedaje) '    
' 1x+3y+2z = 22 (Gastos en comida) ' 
' 1x+1y+1z = 12 (Gastos adicionales) '

' Donde x = Inglaterra, y = Francia, x = España'

A = np.array([[2.0,3.0,2.0],[1.0,3.0,2.0],[1.0,1.0,1.0]])

B = np.array([[27.0],[22.0],[12.0]])

def gaussElimin(a,b):
  n = len(b)
  # Fase de eliminacion
  for k in range(0,n-1):
    for i in range(k+1,n):
      if a[i,k] != 0.0:
        lam = a [i,k]/a[k,k]
        a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
        b[i] = b[i] - lam*b[k]
  # Fase de sustitucion hacia atras
  for k in range(n-1,-1,-1):
    b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
  return b

print(f'El número de dias que el viajero paso fue de:  {gaussElimin(A,B)} en cada país respectivamente.')




' Ejercicio 2 - Posición final de un objeto '

x1 = 0  
v1 = 2 
v2 = 5 
a = 3    
 
' Donde x1 es la posición inicial, v1 es al velocidad inicial, v2 es la velocidad final y a es la aceleración'

' Usando esta ecuación de cinemática para obtener la la diferencia de las posiciones '

d = (v2**2 - v1**2) / (2 * a)

' Sabemos que x2 - x1 = d '

x2 = x1 + d

print(f' La posición final es {x2} metros ')




' Ejercicio 1 - Número complejo '

' Sea z nuestro complejo '

a=5
b=5
z = complex(5,5)

print(z)

r = sqrt(5**2 + 5**2)
theta =  math.acos(a / r)
theta = math.asin(b / r)
print(r)
print(theta)

' Expresamos nuestro número complejo z en forma polar '

print(f'el numero complejo expresado en su forma polar es {'No alcancé profe :( )'}')




























