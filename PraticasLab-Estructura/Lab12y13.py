###Parte01 --Colas

from collections import deque

# 1. Verificar si una palabra es palíndroma
def es_palindroma(palabra):
    # Creamos una cola para almacenar los caracteres de la palabra
    cola = deque()
    for caracter in palabra:
        cola.append(caracter)  # Añadimos cada caracter a la cola
    # Comparamos los caracteres en orden original y reverso para determinar si es palíndroma
    while len(cola) > 1:
        if cola.popleft() != cola.pop():
            return False  # Si los caracteres no coinciden, la palabra no es palíndroma
    return True  # Si todos los caracteres coinciden, la palabra es palíndroma

# 2. Diseño de un sistema de gestión de pedidos
class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = deque()  # Creamos una cola para almacenar los pedidos

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)  # Agregamos un pedido al final de la cola

    def procesar_pedido(self):
        if self.cola_pedidos:
            return self.cola_pedidos.popleft()  # Procesamos el primer pedido de la cola
        else:
            return "No hay pedidos para procesar"  # Si no hay pedidos en la cola

    def mostrar_estado_cola(self):
        return list(self.cola_pedidos)  # Mostramos el estado actual de la cola

# 3. Búsqueda de rutas en un laberinto (BFS)
def encontrar_camino_mas_corto(laberinto, inicio, destino):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    visitado = set()
    cola = deque([(inicio, 0)])  # Usamos una cola para realizar un recorrido BFS
    while cola:
        (fila, columna), distancia = cola.popleft()
        if (fila, columna) == destino:
            return distancia  # Si llegamos al destino, retornamos la distancia
        if (fila, columna) not in visitado:
            visitado.add((fila, columna))
            for df, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nueva_fila, nueva_columna = fila + df, columna + dc
                if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] != '#':
                    cola.append(((nueva_fila, nueva_columna), distancia + 1))
    return -1  # Si no encontramos un camino válido

# 4. Diseño de un sistema de gestión de tareas
class SistemaGestionTareas:
    def __init__(self):
        self.tareas_pendientes = deque()  # Creamos una cola para almacenar las tareas pendientes

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)  # Agregamos una tarea al final de la cola

    def marcar_completada(self):
        if self.tareas_pendientes:
            return self.tareas_pendientes.popleft()  # Marcamos como completada la primera tarea de la cola
        else:
            return "No hay tareas pendientes"  # Si no hay tareas pendientes en la cola

    def mostrar_proxima_tarea(self):
        if self.tareas_pendientes:
            return self.tareas_pendientes[0]  # Mostramos la próxima tarea pendiente
        else:
            return "No hay tareas pendientes"  # Si no hay tareas pendientes en la cola



###Parte02--Árboles
        
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# 5. Contar nodos en el árbol
def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izquierda) + contar_nodos(raiz.derecha)

# 6. Contar nodos hoja en el árbol
def contar_nodos_hoja(raiz):
    if raiz is None:
        return 0
    if raiz.izquierda is None and raiz.derecha is None:
        return 1
    return contar_nodos_hoja(raiz.izquierda) + contar_nodos_hoja(raiz.derecha)

# 7. Contar nodos internos en el árbol
def contar_nodos_internos(raiz):
    if raiz is None or (raiz.izquierda is None and raiz.derecha is None):
        return 0
    return 1 + contar_nodos_internos(raiz.izquierda) + contar_nodos_internos(raiz.derecha)

# 8. Calcular altura del árbol
def calcular_altura(raiz):
    if raiz is None:
        return 0
    return 1 + max(calcular_altura(raiz.izquierda), calcular_altura(raiz.derecha))

# 9. Calcular profundidad de un nodo en el árbol
def calcular_profundidad_nodo(raiz, valor, profundidad=0):
    if raiz is None:
        return -1  # Si el árbol está vacío, no hay profundidad
    if raiz.valor == valor:
        return profundidad  # Si encontramos el nodo con el valor buscado, retornamos su profundidad
    # Recursivamente buscamos en los subárboles izquierdo y derecho
    izquierda = calcular_profundidad_nodo(raiz.izquierda, valor, profundidad + 1)
    derecha = calcular_profundidad_nodo(raiz.derecha, valor, profundidad + 1)
    return max(izquierda, derecha)  # Retornamos la profundidad máxima

# 10. Encontrar el nodo mínimo en el árbol
def encontrar_nodo_minimo(raiz):
    if raiz is None:
        return float('inf')  # Si el árbol está vacío, no hay valor mínimo
    # Recursivamente buscamos el valor mínimo en los subárboles izquierdo y derecho
    return min(raiz.valor, encontrar_nodo_minimo(raiz.izquierda), encontrar_nodo_minimo(raiz.derecha))

# 11. Encontrar el nodo máximo en el árbol
def encontrar_nodo_maximo(raiz):
    if raiz is None:
        return float('-inf')  # Si el árbol está vacío, no hay valor máximo
    # Recursivamente buscamos el valor máximo en los subárboles izquierdo y derecho
    return max(raiz.valor, encontrar_nodo_maximo(raiz.izquierda), encontrar_nodo_maximo(raiz.derecha))


