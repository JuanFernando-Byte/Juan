import matplotlib.pyplot as plt
from math import *
import numpy as np

' Este es el método de Runge-Kutta de orden 4 '

def Run_Kut4(F,x,y,xStop,h):
  def run_kut4(F,x,y,h):
    K0 = h*F(x,y)
    K1 = h*F(x + h/2.0, y + K0/2.0)
    K2 = h*F(x + h/2.0, y + K1/2.0)
    K3 = h*F(x + h, y + K2)
    return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
  
  X = []
  Y = []
  X.append(x)
  Y.append(y)
  
  ' Aqui hacemos que se detenga cuando llegue al final '

  while x < xStop and y[0] < 2.0:  
    h = min(h, xStop - x)
    y = y + run_kut4(F, x, y, h)
    x = x + h
    X.append(x)
    Y.append(y)
    
  return np.array(X), np.array(Y)

' Esto imprime la tabla de resultados'

def imprimeSol(X,Y,frec):
  def imprimeEncabezado(n):
    print("\n t ",end=" ")
    for i in range(n):
      print(f" y[{i}] ",end=" ")
    print()

  def imprimeLinea(x,y,n):
    print("{:13.4e}".format(x),end=" ")
    for i in range(n):
      print("{:13.4e}".format(y[i]),end=" ")
    print() 
  
  m = len(Y)
  try: n = len(Y[0])
  except TypeError: n = 1
  if frec == 0: frec = m
  imprimeEncabezado(n)
  for i in range(0, m, frec):
    imprimeLinea(X[i], Y[i], n)
  if i != m - 1: imprimeLinea(X[m - 1], Y[m - 1], n)


' Aqui definimos la ecuacion diferencial '

def F(t, y):
  g = 9.80665
  r = y[0]
  v = y[1]
  dr_dt = v
  dv_dt = ((pi**2)/12)**2 * r * sin(pi * t)**2 - g * sin((pi/12) * cos(pi * t))
  return np.array([dr_dt, dv_dt])

' Aqui definimos las condiciones iniciales y el intervalo de tiempo '

y = np.array([0.75, 0.0])
t = 0.0
tf = 10.0
h = 0.001

' Aqui evaluamos el método de Runge-Kutta  con las valores dados '
X, Y = Run_Kut4(F, t, y, tf, h)

' Aqui mostramos los resultados'

print('\nEl deslizador alcanza los 2.00 metros en t ≈ {:.4f} segundos'.format(X[-1]))
print('La solución es:')
imprimeSol(X, Y, 500)

' Aqui graficamos los resultados '


plt.plot(X, Y[:,0], label='r(t) - posición del deslizador')
plt.axhline(y=2.0, color='red', linestyle='--', label='r = 2.0 m')    
plt.axvline(x=X[-1], color='red', linestyle='--', label=f't ≈ {X[-1]:.4f} s')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Movimiento del deslizador')
plt.grid()
plt.legend()
plt.show()


























