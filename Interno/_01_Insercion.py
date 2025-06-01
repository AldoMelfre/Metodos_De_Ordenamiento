# Método de Ordenamiento por Inserción
# ------------------------------------
# El método de inserción es un algoritmo sencillo que construye la lista ordenada
# de uno en uno, tomando cada elemento y colocándolo en la posición correcta.
# Es eficiente para listas pequeñas y casi ordenadas, pero lento para listas grandes.

def insercion(lista):
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        clave = lista[i]  # Guardamos el valor actual
        j = i - 1         # Comenzamos a comparar con el elemento anterior

        # Movemos los elementos mayores que la clave una posición adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]  # Desplazamos el elemento hacia adelante
            j -= 1                   # Avanzamos hacia el inicio de la lista

        lista[j + 1] = clave  # Insertamos la clave en la posición correcta

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [5, 2, 9, 1, 5, 6]
    print("Lista original:", datos)
    insercion(datos)
    print("Lista ordenada:", datos)