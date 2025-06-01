# Método de Ordenamiento Externo: Polyphase Sort
# -----------------------------------------------
# Polyphase Sort es una técnica avanzada de ordenamiento externo que utiliza varios archivos
# temporales y distribuye los runs de manera desigual entre ellos, siguiendo una secuencia
# como la de Fibonacci. En cada fase, se fusionan los runs de los archivos menos uno,
# y el archivo restante sirve como destino. Esto minimiza el número de pasadas y el uso de espacio.

import heapq

def polyphase_merge(input_files, output_file):
    # Este es un ejemplo simplificado de la fase de fusión de Polyphase Sort.
    # En la práctica, se requiere una distribución inicial de runs según Fibonacci.
    archivos = [open(f, 'r') for f in input_files]
    heap = []
    
    # Inicializamos el heap con el primer elemento de cada archivo
    for idx, f in enumerate(archivos):
        linea = f.readline()
        if linea:
            heapq.heappush(heap, (int(linea), idx))
    
    with open(output_file, 'w') as fout:
        while heap:
            valor, idx = heapq.heappop(heap)
            fout.write(f"{valor}\n")
            linea = archivos[idx].readline()
            if linea:
                heapq.heappush(heap, (int(linea), idx))
    
    for f in archivos:
        f.close()

# Nota: Un Polyphase Sort completo requiere una distribución inicial de runs en los archivos
# siguiendo la secuencia de Fibonacci y un control cuidadoso de la redistribución de runs
# en cada fase. Este ejemplo muestra solo la fusión multiarchivo, que es la base del método.

# Ejemplo de uso:
# polyphase_merge(['run0.txt', 'run1.txt', 'run2.txt'], 'salida.txt')