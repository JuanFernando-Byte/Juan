'Método de elimincación de Gauss'

'Ejemplo'

import numpy as np

A = np.array([[2,-1,3],[0,2,-1],[7,-5,0]])

B = np.array([[24],[14],[6]])

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

print(f'La intersección de las rectas es {gaussElimin(A,B)}')

'Ecuación lineal de la carga de un protón'

D = np.array([[2.0,1.0],[1.0,2.0]])
E = np.array([[1.0],[0.0]])

print(f'La carga de los Quarks up y down es {gaussElimin(D,E)}')

'Ejemplo Meteoros'

F = np.array([[1,5,10,20],[0,1,-4,0],[-1,2,0,0],[1,1,1,1]])
G = np.array([[95],[0],[1],[26]])
F = F.astype(float)
G = G.astype(float)

print(f'El número asociado a cada masa de los meteoros es {gaussElimin(F,G)}')

