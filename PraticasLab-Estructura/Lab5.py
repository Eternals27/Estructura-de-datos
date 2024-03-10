# 1. Función para devolver un conjunto de números primos
def numeros_primos(conjunto):
    def es_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    return {num for num in conjunto if es_primo(num)}

# 2. Función para devolver un conjunto de palabras que comienzan con una letra determinada
def palabras_con_letra(conjunto, letra):
    return {palabra for palabra in conjunto if palabra.startswith(letra)}

# 3. Función para devolver un conjunto de números divisibles por un número determinado
def numeros_divisibles(conjunto, divisor):
    return {num for num in conjunto if num % divisor == 0}

# 4. Función para devolver un conjunto con los números que están en ambos conjuntos
def interseccion_conjuntos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

# 5. Función para devolver un conjunto con los números que están en el primer conjunto pero no en el segundo
def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

# 6. Función para devolver un conjunto con los números que están en el segundo conjunto pero no en el primero
def diferencia_conjuntos_inversa(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)

# 7. Función para devolver un conjunto con las palabras que son anagramas
def anagramas(conjunto):
    def es_anagrama(palabra1, palabra2):
        return sorted(palabra1) == sorted(palabra2)
    
    anagrama_set = set()
    for palabra1 in conjunto:
        for palabra2 in conjunto:
            if palabra1 != palabra2 and es_anagrama(palabra1, palabra2):
                anagrama_set.add(palabra1)
                anagrama_set.add(palabra2)
    return anagrama_set

# 8. Función para devolver un conjunto con las palabras que son palíndromos
def palindromos(conjunto):
    return {palabra for palabra in conjunto if palabra == palabra[::-1]}

# 9. Función para devolver un conjunto con las palabras que tienen una longitud determinada
def palabras_longitud(conjunto, longitud):
    return {palabra for palabra in conjunto if len(palabra) == longitud}

# 10. Función para devolver un conjunto con las palabras que contienen una letra determinada
def palabras_con_letra(conjunto, letra):
    return {palabra for palabra in conjunto if letra in palabra}

# 11. Función para devolver un conjunto con los números ordenados de menor a mayor
def numeros_ordenados_menor_a_mayor(conjunto):
    return sorted(conjunto)

# 12. Función para devolver un conjunto con los números ordenados de mayor a menor
def numeros_ordenados_mayor_a_menor(conjunto):
    return sorted(conjunto, reverse=True)

# 13. Función para devolver un conjunto con los números duplicados
def numeros_duplicados(conjunto):
    duplicados = set()
    unicos = set()
    for num in conjunto:
        if num in unicos:
            duplicados.add(num)
        else:
            unicos.add(num)
    return duplicados

# 14. Función para devolver un conjunto con los números que no están duplicados
def numeros_no_duplicados(conjunto):
    return conjunto - numeros_duplicados(conjunto)

# 15. Función para devolver un conjunto con los números primos ordenados de menor a mayor
def numeros_primos_ordenados(conjunto):
    return sorted(numeros_primos(conjunto))

# 16. Función para devolver un conjunto con las palabras palíndromas ordenadas de menor a mayor
def palindromos_ordenados(conjunto):
    return sorted(palindromos(conjunto))

# 17. Función para devolver un conjunto con las palabras de longitud determinada ordenadas de menor a mayor
def palabras_longitud_ordenadas(conjunto, longitud):
    return sorted(palabras_longitud(conjunto, longitud))

# 18. Función para devolver un conjunto con las palabras que contienen una letra determinada ordenadas de mayor a menor
def palabras_con_letra_ordenadas(conjunto, letra):
    return sorted(palabras_con_letra(conjunto, letra), reverse=True)

# 19. Función para devolver un conjunto con los números ordenados de menor a mayor y que no están duplicados
def numeros_ordenados_no_duplicados(conjunto):
    return sorted(numeros_no_duplicados(conjunto))

# 20. Función para devolver un conjunto con las palabras palíndromas, de longitud determinada y ordenadas de menor a mayor
def palabras_filtradas_ordenadas(conjunto, longitud):
    return sorted(palabras_longitud(palindromos(conjunto), longitud))
