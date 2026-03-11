import numpy as np


np.random.seed(42)


A = np.random.randint(1, 11, (4, 3))
B = np.random.randint(1, 11, (3, 5))

print("Matricea A:")
print(A)

print("\nMatricea B:")
print(B)


C = A @ B

print("\nProdusul matriceal C = A @ B:")
print(C)


suma = np.sum(C)
media_coloane = np.mean(C, axis=0)
max_global = np.max(C)

print("\nSuma tuturor elementelor din C:", suma)
print("Media pe fiecare coloana:", media_coloane)
print("Valoarea maxima globala:", max_global)