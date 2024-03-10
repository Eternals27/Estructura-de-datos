#1 Operaciones Básicas
def operaciones_basicas():
    # Solicita dos números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Realiza las operaciones básicas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    # Manejo de división por cero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "No es posible dividir por cero"

    # Imprime los resultados
    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", multiplicacion)
    print("División:", division)


#2 Verificación de Número Par o Impar
def verificar_par_impar():
    # Solicita un número al usuario
    numero = int(input("Ingresa un número: "))

    # Verifica si el número es par o impar
    if numero % 2 == 0:
        print(numero, "es un número par.")
    else:
        print(numero, "es un número impar.")


#3 Área de un Triángulo
def area_triangulo():
    # Solicita la base y la altura del triángulo al usuario
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))

    # Calcula el área del triángulo
    area = (base * altura) / 2

    # Imprime el área del triángulo
    print("El área del triángulo es:", area)


#4 Calculadora de Factorial
def factorial(numero):
    # Caso base: factorial de 0 es 1
    if numero == 0:
        return 1
    # Caso recursivo: factorial de n es n * factorial(n - 1)
    else:
        return numero * factorial(numero - 1)


#5 Número Primo
def verificar_primo(numero):
    # Verifica si el número es primo
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                print(numero, "no es un número primo.")
                break
        else:
            print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")


#6 Inversión de Cadena
def invertir_cadena(cadena):
    # Invierte la cadena de texto
    cadena_invertida = cadena[::-1]
    return cadena_invertida


#7 Suma de Números Pares
def suma_numeros_pares(inicio, fin):
    # Suma los números pares en el rango especificado
    suma = 0
    for i in range(inicio, fin + 1):
        if i % 2 == 0:
            suma += i
    return suma


#8 Lista de Cuadrados
def lista_cuadrados():
    # Crea una lista de los cuadrados de los primeros 10 números naturales
    cuadrados = [i ** 2 for i in range(1, 11)]
    return cuadrados


#9 Contador de Vocales
def contar_vocales(cadena):
    # Cuenta el número de vocales en una cadena de texto
    vocales = 'aeiouAEIOU'
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador


#10 Números de la Serie Fibonacci
def fibonacci(n):
    # Genera los primeros n números de la serie Fibonacci
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


#11 Ordenamiento de Lista
def ordenar_lista(lista):
    # Ordena una lista de números ingresados por el usuario de menor a mayor
    lista_ordenada = sorted(lista)
    return lista_ordenada


#12 Palíndromo
def es_palindromo(palabra):
    # Verifica si una palabra es un palíndromo
    palabra = palabra.lower()  # Convertir a minúsculas para evitar diferencias de caso
    return palabra == palabra[::-1]


#13 Generador de Tablas de Multiplicar
def tabla_multiplicar(numero):
    # Genera la tabla de multiplicar de un número ingresado por el usuario
    tabla = []
    for i in range(1, 11):
        tabla.append(numero * i)
    return tabla


#14 Cálculo del Área de un Círculo
def area_circulo(radio):
    # Calcula el área de un círculo
    import math
    area = math.pi * radio ** 2
    return area


#15 Suma de Dígitos
def suma_digitos(numero):
    # Toma un número entero y calcula la suma de sus dígitos
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

