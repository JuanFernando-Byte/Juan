import sys
import math
from numpy import sign
from math import *

' Tarea 4 - Raíces,Diferencia,Integración - Juan Fernando De Los Ríos Guerrero '

' Ejercicio 1 - Repeat Prob. 10 with the Newton-Raphson method '

' Aquí definimos la función original y la derivada de ella'

def f(x):
    return x * math.sin(x) + 3 * math.cos(x) - x
def df(x):
    return x * math.cos(x) - 2 * math.sin(x) - 1


def err(string):
    print(string)
    input('Press return to exit')
    sys.exit()

'Aqui definimos el método Newton-Raphson'

def newtonRaphson(f, df, a, b, tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): err('La raíz no está en el intervalo')

    x = 0.5 * (a + b)
    for i in range(30):
        print(f"Iteración {i}, x = {x:.6f}")
        fx = f(x)
        if fx == 0.0:
            return x
        if sign(fa) != sign(fx):
            b = x
        else:
            a = x
        try:
            dx = -fx / df(x)
        except ZeroDivisionError:
            dx = b - a

        x = x + dx

        if (b - x) * (x - a) < 0.0:
            dx = 0.5 * (b - a)
            x = a + dx

        if abs(dx) < tol * max(abs(b), 1.0):
            return x
    print('Demasiadas iteraciones en Newton-Raphson')
    return None

' Esta función nos ayuda a buscar el cambio de signo en el intervalo '

def rootsearch(f, a, b, dx):
    x1 = a
    f1 = f(x1)
    while x1 < b:
        x2 = x1 + dx
        if x2 > b:
            x2 = b
        f2 = f(x2)
        if f1 * f2 <= 0:
            return x1, x2
        x1 = x2
        f1 = f2
    return None, None

' Aqui usamos el metodo de Newton-Raphson para encontrar las raices'

# Tuve que agregar esto por que de otro modo me salia que no habia raices
# en el intervalo dado

def find_roots(f, df, a, b, dx=0.1, tol=1.0e-6):
    roots = []
    while a < b:
        x1, x2 = rootsearch(f, a, b, dx)
        if x1 is None:
            break
        root = newtonRaphson(f, df, x1, x2, tol)
        if root is not None:
            if not any(abs(root - r) < tol for r in roots):
                roots.append(root)
        a = x2
    return roots


roots = find_roots(f, df, -6, 6)

print("\nRaíces encontradas en (-6, 6):")
for r in roots:
    print(f"x = {r:.6f}, f(x) = {f(r):.2e}")








' Ejercicio 2 - Cohete Saturn V '

' Aqui tenemos los valores iniciales '

u = 2510         
M0 = 2.8e6         
m = 13.3e3        
g = 9.81           

' Aqui definimos la funcion y su derivada'

def f(t):
    return u * math.log(M0 / (M0 - m * t)) - g * t - 335

def df(t):
    return (u * m) / (M0 - m * t) - g


def err(string):
    print(string)
    input('Presiona enter para salir...')
    sys.exit()

' Aqui definimos el metodo Newton-Raphson '

def newtonRaphson(f, df, a, b, tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): err('La raíz no está en el intervalo')

    x = 0.5 * (a + b)
    for i in range(30):
        fx = f(x)
        if fx == 0.0: return x
        if sign(fa) != sign(fx):
            b = x
        else:
            a = x
        dfx = df(x)
        try:
            dx = -fx / dfx
        except ZeroDivisionError:
            dx = b - a
        x = x + dx
        if (b - x) * (x - a) < 0.0:
            dx = 0.5 * (b - a)
            x = a + dx
        if abs(dx) < tol * max(abs(b), 1.0):
            return x
    print('Demasiadas iteraciones en Newton-Raphson')
    return None

a, b = 5.0, 100.0
root = newtonRaphson(f, df, a, b)
if root is not None:
    print(f"\nEl cohete alcanza la velocidad del sonido en t = {root:.6f} segundos.")
else:
    print("No se encontró solución.")








'Ejercicio 3 - Use the data in the table to compute f(0.2) as accurately as possible:'

' Diferencias finitas '


' Aqui solo definimos los datos de la tabla '
# tuve que agregar el cilco for por que me daba error 

def f(x):
    
    x_vals = [0.0, 0.1, 0.2, 0.3, 0.4]
    f_vals = [0.000000, 0.078348, 0.138910, 0.192916, 0.244981]
    
    for i in range(len(x_vals)):
        if isclose(x_vals[i], x, abs_tol=1e-9): 
            return f_vals[i]

    raise ValueError(f"{x} no está en la lista de valores de x.")


def isclose(a, b, abs_tol=1e-9):
    return abs(a - b) <= abs_tol

' Aqui definimos las funciones para calcular la derivada '

' Aproximación central '

def df2c(x, h):  
    return (f(x+h) - f(x-h)) / (2*h)

' Aproximación backward '

def df2b(x, h):  
    return (f(x) - f(x-h)) / h

' Aproximación forward '

def df2f(x, h):  
    return (f(x+h) - f(x)) / h


x = 0.2
h = 0.1

' Aqui calculamos las derivadas con los valores de x y h'

df_central = df2c(x, h)
df_backward = df2b(x, h)
df_forward = df2f(x, h)

print(f"Derivada central en x = {x}: {df_central}")
print(f"Derivada backward en x = {x}: {df_backward}")
print(f"Derivada forward en x = {x}: {df_forward}")







' Ejercicio 4 - determine d(sin x)/dx at x = 0.8 '

' Aqui definimos la funcion inicial y su derivada '

def f(x):
    return math.sin(x)

def exact_derivative(x):
    return math.cos(x)

' Aqui definimos las aproximaciones'

def df(x, h):
    return (f(x + h) - f(x)) / h

def dc(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

' Aqui h tiene muchos valores puesto el ejercicio pedia que requeriria de experimentación '

x = 0.8
h_values = [0.1, 0.05, 0.01, 0.005, 0.001]
exact = exact_derivative(x)

' Aqui iremos almacenando los resultados en cada una de las aproximaciones '
resultados_forward = []
resultados_central = []

' Aqui probamos con cada uno de los valores de h con lsa aproximaciones forward y central'
for h in h_values:
    df_result = df(x, h)
    dc_result = dc(x, h)
    resultados_forward.append((h, df_result, abs(df_result - exact)))
    resultados_central.append((h, dc_result, abs(dc_result - exact)))


print('Resultados de diferencia forward:')
for h, result, error in resultados_forward:
    print(f'h = {h: .4f} -> Result: {result:.5f}, Error: {error:.5f}')

print('Resultados de diferencia central:')
for h, result, error in resultados_central:
    print(f'h = {h: .4f} -> Result: {result:.5f}, Error: {error:.5f}')





' Ejercicio 5 - Integral '


' Aqui definimos la función que nos da el ejercicio'

def f(x):
    return math.log(1 + math.tan(x))

Iold = 0.0

' Aqui definimos la regra trapezoidal recursiva'

def trapecio_recursiva(f, a, b, Iold, k):
    n = 2 ** (k - 1)
    h = (b - a) / n  
    
    sum_f = (f(a) + f(b)) / 2
    
    for i in range(1, n):
        sum_f += f(a + i * h)
    
    Inew = h * sum_f
    
    if k > 1:
        Inew = (4 ** (k - 1) * Inew - Iold) / (4 ** (k - 1) - 1)
    
    return Inew


' Aqui calculamos la integral '

for k in range(1, 21):
    Inew = trapecio_recursiva(f, 0.0, math.pi / 4, Iold, k)
    
    
    if (k > 1) and (abs(Inew - Iold)) < 1.0e-6:
        break
    
    Iold = Inew


print('Integral =', Inew)
print('n Panels =', 2**(k - 1))



























