# Método de Ordenamiento por Árbol (Heap Sort)
# ---------------------------------------------
# El ordenamiento por árbol, conocido como Heap Sort, utiliza una estructura de datos
# llamada heap (montículo) para ordenar los elementos. Primero construye un heap máximo,
# luego extrae el elemento mayor y lo coloca al final de la lista, repitiendo el proceso.
# Es más eficiente que los métodos simples para listas grandes.

def heapify(lista, n, i):
    # Función para mantener la propiedad del heap
    mayor = i  # Suponemos que el nodo actual es el mayor
    izq = 2 * i + 1  # Índice del hijo izquierdo
    der = 2 * i + 2  # Índice del hijo derecho

    # Si el hijo izquierdo es mayor que el nodo actual
    if izq < n and lista[izq] > lista[mayor]:
        mayor = izq

    # Si el hijo derecho es mayor que el nodo actual
    if der < n and lista[der] > lista[mayor]:
        mayor = der

    # Si el mayor no es el nodo actual, intercambiamos y continuamos heapificando
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]  # Intercambio
        heapify(lista, n, mayor)  # Heapificamos el subárbol afectado

def heap_sort(lista):
    n = len(lista)  # Obtenemos la longitud de la lista

    # Construimos un heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Extraemos elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Movemos el mayor al final
        heapify(lista, i, 0)  # Heapificamos el heap reducido

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [12, 11, 13, 5, 6, 7]
    print("Lista original:", datos)
    heap_sort(datos)
    print("Lista ordenada:", datos)