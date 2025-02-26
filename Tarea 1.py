
# Clase 1

'''

'Ejercicio 1'

# Elabora un programa que calcule la temperatura en grados celsius a partir de la temperatura en grados fahrenheit.

import math

temp_f = float(input('Ingrese la temperatura en grados fahrenheit:'))

temp_c = (temp_f - 32) * 5/9

print(f'La temperatura {temp_f} en grados celsius es: {temp_c}')

'''

'''

'Ejercicio  2'

import math

x = 5

a = math.sinh(5)

print('El seno hiperbolico de 5 es: ',a)

b = (math.e**x - math.exp**-(x))/2

print(f'La ecuación es igual a {b}')

c = (math.exp(x)-math.exp(-x))/2

print(f'la ecuación es igual a {c}')

'''

'''

'Ejercicio en clase de complejos'

z1 = 8 + 4j
z2 = 2j
w = z1 + z2
s = complex(5,6)
print(z1)
print(z2)
print(w)
print(s)

a = 4
b = -2.3
z = a + b*1j
z.real # Extrae la parte de real del numero complejo
z.conjugate # Extrae la parte conjugada del numero complejo
print(z)
print(z.real)

'''

# Clase 2

'''

# Método de descomposición Doolittle

import numpy as np

def doolittle_lu(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        # Calcular elementos de U
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
        
        # Poner 1 en la diagonal de L
        L[i, i] = 1
        
        # Calcular elementos de L
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
    
    return L, U

# Ejemplo de uso
A = np.array([[2, -1, 1],
              [3, 3, 9],
              [3, 3, 5]], dtype=float)

L, U = doolittle_lu(A)

print("Matriz L:")
print(L)
print("\nMatriz U:")
print(U)

'''

'''

# Clase 3

from cmath import sin, sinh, exp

r1 = sin(8j)
a = exp(5j)

'Ejercicio 3' 

# 1. Considera la relación entre el seno en variable compleja y el seno hiperbólico en variable real x,

# sin(ix) = sinh(x)

# En tu portafolio de clase, elabora un programa que calcule el valor de sin(ix) y de sinh(x) para ciertos valores dados de x, para verificar la identidad.

import math
from cmath import sin, sinh, cos, e, exp

x = complex(input('ingrese un numero:\n'))
x1=float(x)
print('sin(i',x,')=' , sin(x*1j))
print('isin(',x,')=' , 1j*sinh(x))

# 2. Considera la relación de Euler para x real,

# e^{ix} = cos(x) + sin(x)

# En tu portafolio de clase, elabora un programa que calcule el valor de cos(x), sin(x) y de e^{ix} para ciertos valores dados de x, para verificar la identidad

n = complex(input('Ingrese un numero:\n'))
ne = exp(1j*n)
nt = cos(n)+1j*sin(n)
print(f'Su numero es {ne}')
print(f'Su numero con la relacion coseno + seno es {nt}')

'''

'''

'Ejercicio 4'

# En tu portafolio de clase, elabora un programa en el que uses Numpy 
# para calcular el valor de las raices con diferentes valores dados de 
# a,b,c, para obtener ejemplos de raices reales y complejas.

import numpy as np

def discriminante(a,b,c):

    discriminante = b**2 - 4*a*c

    if discriminante >= 0:

        r1 = (-b + np.sqrt(discriminante))/(2*a)
        r2 = (-b - np.sqrt(discriminante))/(2*a)
    
    else:

        componente_imaginaria = np.sqrt(abs(discriminante)) / (2*a)
        componente_real = -b / (2*a)

        r1 = complex (componente_real, componente_imaginaria)
        r2 = complex (componente_real, -componente_imaginaria)

    return r1, r2

a = float(input('Ingrese los coeficientes de la función cuadrática f(z) = az^2 + bz + c, el coeficiente a es: '))

b = float(input('Ingrese el coeficiente b: '))

c = float(input('Ingrese el coeficiente c: '))

r1,r2 = discriminante(a,b,c)

print(f'Las raices de la función f(z)={a}z²+{b}z+{c} son: {r1} y {r2}')

'''

'''

'Ejericico 5'

import math
import numpy as np

def trayectoria(v0, theta, y0, x):
    g = 9.81  
    theta_rad = np.radians(theta)
    
    
    y = y0 + x * np.tan(theta_rad) - (g * x**2) / (2 * v0**2 * np.cos(theta_rad)**2)
    
    return y

v0 = float(input("Ingresa la velocidad inicial (v0) en m/s: "))
theta = float(input("Ingresa el ángulo de lanzamiento (θ) en grados: "))
y0 = float(input("Ingresa la altura inicial (y0) en metros: "))
x = float(input("Ingresa la distancia horizontal (x) en metros: "))


y = trayectoria(v0, theta, y0, x)

print("\nResultados:")
print(f"Trayectoria en y(x) = {y} metros")

'''
 





























