
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

' Examen 2 - Juan Fernando De Los Ríos Guerrero '



' Ejercicio 1 '

' Calcular con una presicion de cuatro cifras significativas '


def err(string):
    print(string)
    input('Press return to exit')
    sys.exit()

def newtonRaphson(f, df, a, b, tol=1.0e-9):
    from numpy import sign
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): err('La raíz no está en el intervalo')
    x = 0.5 * (a + b)
    for i in range(30):
        print(i)
        fx = f(x)
        if fx == 0.0: return x
        if sign(fa) != sign(fx): b = x
        else: a = x
        dfx = df(x)
        try:
            dx = -fx / dfx
        except ZeroDivisionError:
            dx = b - a
        x = x + dx
        if (b - x) * (x - a) < 0.0:
            dx = 0.5 * (b - a)
            x = a + dx
        if abs(dx) < tol * max(abs(b), 1.0): return x
    print('Too many iterations in Newton-Raphson')

def f1(x): return x**3 - 75
def df1(x): return 3 * x**2

root = newtonRaphson(f1, df1, 4.0, 5.0)
print(f'\nResultado: ∛75 ≈ {root:.4g}')

' Aqui graficamos '

x_vals = np.linspace(3.5, 5.0, 400)
y_vals = f1(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='$f(x) = x^3 - 75$', color='blue')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f'Raíz ≈ {root:.4g}')
plt.title('Gráfica de $f(x) = x^3 - 75$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()





' Ejercicio 2 '

' Encuentra la raiz positiva real mas pequeña de la ecuación '

# Metodo de Biseccion Mejorado para el Ejemplo de clase

' Aqui definimos la funcion con la ecuacion dada en el ejercicio '

def y(x):                    # Define la funcion y(x)
    y = x**3 - 3.23*x**2 - 5.54*x + 9.84
    return y

x1 = float(input('Captura el valor de x1: '))  # Petición de valor x1
x2 = float(input('Captura el valor de x2: '))  # Petición de valor x2
y1 = y(x1)                                     # Evalúa la función en x1
y2 = y(x2)                                     # Evalúa la función en x2

if y1 * y2 > 0:                                # prueba si los signos son iguales
    print('No hay raíces en el intervalo.')
    exit()

for i in range(100):
    xh = (x1 + x2) / 2
    yh = y(xh)                                # evalua la funcion y(xh)
    if abs(yh) < 1.0e-6:
        break
    elif y1 * yh < 0: 
        x2 = xh
    else:  
        x1 = xh


print('La raíz es: %.5f' % xh)  
print('Número de bisecciones: %d' % (i + 1))





' Ejercicio 3 '

' Utilice aproximaciones por diferencias finitas '


' Aqui definimos la funcion que usaremos para los valores que nos dieron'

def f(x, tabla):
    return tabla[x]

' Aqui definimos la primera derivada central '

def d1fc(x, h, tabla): 
    return (f(x + h, tabla) - f(x - h, tabla)) / (2 * h)


' Aqui definimos la segunda derivada central '

def d2fc(x, h, tabla):
    return (f(x + h, tabla) + f(x - h, tabla) - 2 * f(x, tabla)) / (h**2)

' Estos son los valores que se nos dieron '


valores = {
    2.36: 0.85866,
    2.37: 0.86289,
    2.38: 0.86710,
    2.39: 0.87129
}

h = 0.01

x0 = 2.36

' Aqui evaluamos con el valor dado '


primeracentral = d1fc(x0, h, valores)
segundacentral = d2fc(x0, h, valores)

print(f"f'(2.36) (Central) ≈ {primeracentral:.5f}")
print(f"f''(2.36) (Central) ≈ {segundacentral:.5f}")




' Ejercicio 4 '

' Regla trapezoidal recursiva '


' Aqui hacemos un cambio de variable para eliminar la singularidad '

def f(t):
    return math.sin(t**2)


def trapecio_recursiva(f, a, b, Iold, k):
    if k == 1:
        Inew = (f(a) + f(b)) * (b - a) / 2.0
    else:
        n = 2 ** (k - 2)
        h = (b - a) / n
        x = a + h / 2.0
        sum = 0.0
        
    
        for i in range(n):
            sum = sum + f(x)
            x = x + h
        
        Inew = (Iold + h * sum) / 2.0
    return Inew

' Aqui tenemos nuestros limites de integración'
a, b = 0, 1


Iold = (f(a) + f(b)) * (b - a) / 2.0


for k in range(1, 21):
    Inew = trapecio_recursiva(f, a, b, Iold, k)
    if (k > 1) and (abs(Inew - Iold)) < 1.0e-6:
        break
    Iold = Inew


print('Integral =', Inew)
print('n Panels =', 2**(k-1))

































