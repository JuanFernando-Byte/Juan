
'Descomposición de matrices'

# Algoritmo del método descomposición Doolittle

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


































