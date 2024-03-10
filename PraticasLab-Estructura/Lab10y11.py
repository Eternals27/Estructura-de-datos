##Parte 01

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# 1. Duplicar Nodos
def duplicar_nodos(lista):
    actual = lista
    while actual is not None:
        # Crear un nuevo nodo con el mismo dato que el nodo actual
        nuevo_nodo = NodoDoble(actual.dato)
        # Insertar el nuevo nodo entre el nodo actual y el siguiente
        siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual
        nuevo_nodo.siguiente = siguiente
        if siguiente:
            siguiente.anterior = nuevo_nodo
        actual = siguiente

# 2. Contar Nodos Pares e Impares
def contar_nodos_pares_impares(lista):
    contador_pares = 0
    contador_impares = 0
    actual = lista
    while actual is not None:
        # Contar nodos con datos pares e impares
        if actual.dato % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
        actual = actual.siguiente
    return contador_pares, contador_impares

# 3. Insertar Nodo en Posición Específica
def insertar_nodo_en_posicion(lista, dato, posicion):
    nuevo_nodo = NodoDoble(dato)
    if posicion == 1:
        # Insertar el nuevo nodo al principio de la lista
        nuevo_nodo.siguiente = lista
        lista.anterior = nuevo_nodo
        return nuevo_nodo
    actual = lista
    for _ in range(1, posicion - 1):
        # Avanzar hasta la posición deseada
        if actual is None:
            return lista
        actual = actual.siguiente
    if actual is None:
        return lista
    siguiente = actual.siguiente
    actual.siguiente = nuevo_nodo
    nuevo_nodo.anterior = actual
    nuevo_nodo.siguiente = siguiente
    if siguiente:
        siguiente.anterior = nuevo_nodo
    return lista

# 4. Eliminar Nodos Duplicados
def eliminar_nodos_duplicados(lista):
    actual = lista
    while actual is not None:
        dato = actual.dato
        siguiente = actual.siguiente
        while siguiente is not None and siguiente.dato == dato:
            # Eliminar nodos duplicados
            siguiente = siguiente.siguiente
        actual.siguiente = siguiente
        if siguiente:
            siguiente.anterior = actual
        actual = siguiente

# 5. Invertir la Lista
def invertir_lista(lista):
    actual = lista
    while actual.siguiente is not None:
        actual = actual.siguiente
    ultimo = actual
    while ultimo is not None:
        # Imprimir la lista en orden inverso
        print(ultimo.dato)
        ultimo = ultimo.anterior


####Parte 02
        
## Implementación de una pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

# 6. Invertir una cadena utilizando una pila
def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    cadena_invertida = ''
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    return cadena_invertida

# 7. Convertir número decimal a binario utilizando una pila
def decimal_a_binario(numero):
    pila = Pila()
    while numero > 0:
        residuo = numero % 2
        pila.apilar(residuo)
        numero //= 2
    binario = ''
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    return binario

# 8. Evaluar expresión posfija utilizando una pila
def evaluar_expresion_posfija(expresion):
    pila = Pila()
    for caracter in expresion.split():
        if caracter.isdigit():
            pila.apilar(int(caracter))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if caracter == '+':
                pila.apilar(operando1 + operando2)
            elif caracter == '-':
                pila.apilar(operando1 - operando2)
            elif caracter == '*':
                pila.apilar(operando1 * operando2)
            elif caracter == '/':
                pila.apilar(operando1 / operando2)
    return pila.desapilar()

# 9. Validar operadores anidados utilizando una pila
def validar_operadores_anidados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter in '([{':
            pila.apilar(caracter)
        elif caracter in ')]}':
            if pila.esta_vacia():
                return False
            tope = pila.desapilar()
            if (caracter == ')' and tope != '(') or \
               (caracter == ']' and tope != '[') or \
               (caracter == '}' and tope != '{'):
                return False
    return pila.esta_vacia()
