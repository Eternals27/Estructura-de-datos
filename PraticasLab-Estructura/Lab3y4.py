## Recursividad

# Ejercicio 1: Imprimir números pares del 1 al 100
def imprimir_pares(n):
    if n <= 0:
        return
    imprimir_pares(n - 1)
    if n % 2 == 0:
        print(n, end=" ")

# Ejercicio 2: Suma de números del 1 al n
def suma_hasta_n(n):
    if n == 0:
        return 0
    return n + suma_hasta_n(n - 1)

# Ejercicio 3: Imprimir pirámide de números del 1 al n
def imprimir_piramide_ascendente(n):
    if n <= 0:
        return
    imprimir_piramide_ascendente(n - 1)
    print(" ".join(str(i) for i in range(1, n + 1)))

# Ejercicio 4: Imprimir pirámide de números invertidos del 1 al n
def imprimir_piramide_descendente(n):
    if n <= 0:
        return
    print(" ".join(str(i) for i in range(1, n + 1)))
    imprimir_piramide_descendente(n - 1)

# Ejercicio 5: Imprimir tabla de multiplicar del n
def tabla_multiplicar_recursiva(n, i=1):
    if i > 10:
        return
    print(f"{n} x {i} = {n * i}")
    tabla_multiplicar_recursiva(n, i + 1)


## Arreglos y Matrices

import numpy as np

# Ejercicio 6: Crear una matriz de números reales
matriz_reales = np.random.rand(3, 3)

# Ejercicio 7: Crear una matriz de números complejos
matriz_complejos = np.random.rand(3, 3) + np.random.rand(3, 3) * 1j

# Ejercicio 8: Crear una matriz de matrices
matriz_de_matrices = np.array([[np.random.rand(2, 2) for _ in range(3)] for _ in range(3)])

# Ejercicio 9: Acceder al elemento central de una matriz
def elemento_central(matriz):
    filas, columnas = matriz.shape
    return matriz[filas // 2, columnas // 2]

# Ejercicio 10: Sumar dos matrices de diferentes tamaños
def sumar_matrices(matriz1, matriz2):
    if matriz1.shape != matriz2.shape:
        return "Las matrices tienen diferentes dimensiones"
    return matriz1 + matriz2

# Ejercicio 11: Multiplicar una matriz por un número
def multiplicar_por_numero(matriz, numero):
    return matriz * numero

# Ejercicio 12: Calcular la media de los elementos de una matriz
def media_matriz(matriz):
    return np.mean(matriz)


#### Ejercicio parte 01:

# Ejercicio 1: Crear una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)

# Ejercicio 2: Calcular la media, la mediana y la desviación estándar de los elementos de una matriz
def estadisticas_matriz(matriz):
    media = np.mean(matriz)
    mediana = np.median(matriz)
    desviacion_estandar = np.std(matriz)
    return media, mediana, desviacion_estandar

# Ejercicio 3: Encontrar el elemento máximo de una matriz
def elemento_maximo(matriz):
    return np.max(matriz)

# Ejercicio 4: Encontrar la submatriz de mayor suma de una matriz
def submatriz_maxima(matriz):
    filas, columnas = matriz.shape
    max_suma = 0
    indices = None
    for i in range(filas):
        for j in range(columnas):
            for k in range(i + 1, filas + 1):
                for l in range(j + 1, columnas + 1):
                    suma = np.sum(matriz[i:k, j:l])
                    if suma > max_suma:
                        max_suma = suma
                        indices = ((i, j), (k - 1, l - 1))
    return indices

# Ejercicio 5: Encontrar la matriz de covarianza de dos matrices
def matriz_covarianza(matriz1, matriz2):
    return np.cov(matriz1, matriz2)


# Recursividad
print("Ejercicio 1: Números pares del 1 al 100:")
imprimir_pares(100)
print("\nEjercicio 2: Suma de números del 1 al n (n=10):", suma_hasta_n(10))
print("\nEjercicio 3: Pirámide de números del 1 al n (n=5):")
imprimir_piramide_ascendente(5)
print("\nEjercicio 4: Pirámide de números invertidos del 1 al n (n=5):")
imprimir_piramide_descendente(5)
print("\nEjercicio 5: Tabla de multiplicar del 5:")
tabla_multiplicar_recursiva(5)

# Arreglos y Matrices
print("\nMatriz de números reales:")
print(matriz_reales)
print("\nMatriz de números complejos:")
print(matriz_complejos)
print("\nMatriz de matrices:")
print(matriz_de_matrices)
print("\nElemento central de la matriz de números reales:")
print(elemento_central(matriz_reales))
print("\nSuma de matrices:")
print(sumar_matrices(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])))
print("\nMatriz multiplicada por un número:")
print(multiplicar_por_numero(np.array([[1, 2], [3, 4]]), 5))
print("\nMedia de la matriz de números reales:")
print(media_matriz(matriz_reales))
print("\nMatriz de números aleatorios de tamaño 100x100:")
print(matriz_aleatoria)
print("\nEstadísticas de la matriz de números aleatorios:")
print(estadisticas_matriz(matriz_aleatoria))
print("\nElemento máximo de la matriz de números aleatorios:")
print(elemento_maximo(matriz_aleatoria))
print("\nSubmatriz de mayor suma de la matriz de números aleatorios:")
print(submatriz_maxima(matriz_aleatoria))
print("\nMatriz de covarianza entre la matriz de números reales y la matriz de números complejos:")
print(matriz_covarianza(matriz_reales, matriz_complejos))
