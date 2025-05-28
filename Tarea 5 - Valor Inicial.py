import numpy as np
from numpy import sqrt
from scipy.integrate import solve_ivp


' Tarea 5 - Valor Inicial - Juan Fernando De Los Ríos Guerrero '

' Ejercicio 1 '



' Aquí definimos la función F(x,y) que representa la ecuación diferencial '

def F(x, y):
    return np.sin(y)

' Este es el método de Euler para la integración numérica '

def eulerint(F, x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h, xStop - x)
        y = y + h * F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

' Esta función es para imprimir los resultados de la integración '

def imprimeSol(X, Y, frec):
    def imprimeEncabezado(n):
        print("\n x ", end=" ")
        for i in range(n):
            print(" y[", i, "] ", end=" ")
        print()

    def imprimeLinea(x, y, n):
        print("{:13.4e}".format(x), end=" ")
        for i in range(n):
            print("{:13.4e}".format(y[i]), end=" ")
        print()

    m = len(Y)
    try:
        n = len(Y[0])
    except TypeError:
        n = 1
    imprimeEncabezado(n)
    for i in range(0, m, frec):
        imprimeLinea(X[i], np.atleast_1d(Y[i]), n)
    if (m - 1) % frec != 0:
        imprimeLinea(X[m - 1], np.atleast_1d(Y[m - 1]), n)

' Aqui establecemos las condiciones iniciales '

x0 = 0
y0 = 1
xStop = 0.5
h = 0.1

' Aqui evaluamos el método de Euler e imprimimos los resultados '

X, Y = eulerint(F, x0, y0, xStop, h)
imprimeSol(X, Y, 1)







' Ejercicio 2 '



' Aquí definimos la función F(x,y) que representa la ecuación diferencial '

def F(x, y):
    return y**(1/3)

' Este es el método de Euler para la integración numérica '

def eulerint(F, x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h, xStop - x)
        y = y + h * F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

' Esta función es para imprimir los resultados de la integración '

def imprimeSol(X, Y, frec):
    def imprimeEncabezado(n):
        print("\n x ", end=" ")
        for i in range(n):
            print(" y[", i, "] ", end=" ")
        print()

    def imprimeLinea(x, y, n):
        print("{:13.4e}".format(x), end=" ")
        for i in range(n):
            print("{:13.4e}".format(y[i]), end=" ")
        print()

    m = len(Y)
    try:
        n = len(Y[0])
    except TypeError:
        n = 1
    imprimeEncabezado(n)
    for i in range(0, m, frec):
        imprimeLinea(X[i], np.atleast_1d(Y[i]), n)
    if (m - 1) % frec != 0:
        imprimeLinea(X[m - 1], np.atleast_1d(Y[m - 1]), n)


' Aqui establecemos las condiciones iniciales '

x0 = 0
xStop = 1.0
h = 0.1

' Aqui evaluamos el método de Euler e imprimimos los resultados para los dos casos '

print('Caso (a): y(0) = 0')
X1, Y1 = eulerint(F, x0, 0.0, xStop, h)
imprimeSol(X1, Y1, 1)

print('\nCaso (b): y(0) = 1e-16')
X2, Y2 = eulerint(F, x0, 1e-16, xStop, h)
imprimeSol(X2, Y2, 1)







' Ejercicio 3 '



' Este es el método de Ridder ' 

def Ridder(f, a, b, tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if np.sign(fa) != np.sign(fb): c = a; fc = fa
    for i in range(30):
        c = 0.5 * (a + b)
        fc = f(c)
        s = sqrt(fc**2 - fa * fb)
        if s == 0.0: return None
        dx = (c - a) * fc / s
        if (fa - fb) < 0.0:
            dx = -dx
        x = c + dx
        fx = f(x)
        if i > 0 and abs(x - xOld) < tol * max(abs(x), 1.0):
            return x
        xOld = x
        if np.sign(fc) == np.sign(fx):
            if np.sign(fa) != np.sign(fx):
                b = x
                fb = fx
            else:
                a = x
                fa = fx
        else:
            a = c
            b = x
            fa = fc
            fb = fx
    print("Demasiadas iteraciones")
    return None

' Aqui definimos las ecuaciones diferenciales para el inciso (a) '
' Use solve_ivp  que es muy util para resolver el problema de valor inicial '
' Ya que integra desde las condiciones iniciales en este caso de 0 a 1 '

def ode_a(x, Y):
    y1, y2 = Y
    return [y2, -np.exp(-y1)]

def f_a(s):
    sol = solve_ivp(ode_a, [0, 1], [1, s], t_eval=[1])
    return sol.y[0, -1] - 0.5

' Aqui definimos las ecuaciones diferenciales para el inciso (c) '

def ode_c(x, Y):
    y1, y2 = Y
    return [y2, np.cos(x * y1)]

def f_c(s):
    sol = solve_ivp(ode_c, [0, 1], [0, s], t_eval=[1])
    return sol.y[0, -1] - 2

' Ahora aplicamos el método de Ridder para encontrar las soluciones '

s_a = Ridder(f_a, -2.0, 2.0)
s_c = Ridder(f_c, 1.0, 6.0)

' Aquí imprimimos los resultados '

print(f"Inciso (a): y'(0) ≈ {s_a:.5f}")
print(f"Inciso (c): y'(0) ≈ {s_c:.5f}")























