#### Parte 01

# 1. Validar la edad de un usuario.
def validar_edad(edad):
    return edad >= 18

# 2. Verificar el tipo de dato de una variable.
def verificar_tipo(variable, tipo):
    return isinstance(variable, tipo)

# 3. Validar el rango de una calificación.
def validar_calificacion(calificacion):
    return 0 <= calificacion <= 10

# 4. Asegurar que una lista no esté vacía.
def lista_no_vacia(lista):
    return bool(lista)

# 5. Validar la igualdad de dos objetos.
def validar_igualdad(objeto1, objeto2):
    return objeto1 == objeto2

# 6. Asegurar que un ciclo while se ejecuta al menos una vez.
def ciclo_while_al_menos_una_vez(condicion):
    while True:
        if condicion:
            break

# 7. Asegurar que una función retorna un valor específico.
def funcion_retorna_valor(valor_esperado):
    def funcion():
        return valor_esperado
    return funcion

# 8. Validar el estado de una variable después de una operación.
def validar_estado_variable(var, operacion, resultado_esperado):
    return var == operacion == resultado_esperado

# 9. Asegurar que un módulo se ha importado correctamente.
def modulo_importado(modulo):
    return modulo in globals()


#### Parte 02

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# 10. Desarrollar el código de buscar nodo en la lista enlazada simple.
def buscar_nodo(lista, valor):
    actual = lista
    while actual is not None:
        if actual.valor == valor:
            return True
        actual = actual.siguiente
    return False

# 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
def suma_nodos(lista):
    suma = 0
    actual = lista
    while actual is not None:
        suma += actual.valor
        actual = actual.siguiente
    return suma

# 12. Crea una función que devuelva la longitud de una lista enlazada simple.
def longitud_lista(lista):
    longitud = 0
    actual = lista
    while actual is not None:
        longitud += 1
        actual = actual.siguiente
    return longitud

# 13. Implementa una función que concatene dos listas enlazadas simples.
def concatenar_listas(lista1, lista2):
    if lista1 is None:
        return lista2
    actual = lista1
    while actual.siguiente is not None:
        actual = actual.siguiente
    actual.siguiente = lista2
    return lista1

# 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
def eliminar_duplicados(lista):
    nodos_vistos = set()
    anterior = None
    actual = lista
    while actual is not None:
        if actual.valor in nodos_vistos:
            anterior.siguiente = actual.siguiente
        else:
            nodos_vistos.add(actual.valor)
            anterior = actual
        actual = actual.siguiente

# 15. Implementa una función que invierta el orden de una lista enlazada simple.
def invertir_lista(lista):
    anterior = None
    actual = lista
    siguiente_nodo = None
    while actual is not None:
        siguiente_nodo = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente_nodo
    lista = anterior
    return lista
