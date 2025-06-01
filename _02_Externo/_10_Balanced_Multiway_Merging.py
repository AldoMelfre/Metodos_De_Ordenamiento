# Método de Ordenamiento Externo: Balanced Multiway Merging
# ---------------------------------------------------------
# Balanced Multiway Merging es una técnica de ordenamiento externo donde se utilizan
# varios archivos temporales (más de dos) para almacenar y fusionar los runs.
# En cada pasada, los runs se distribuyen equitativamente entre los archivos y luego
# se fusionan en uno o más archivos de salida, repitiendo el proceso hasta que todo
# el archivo esté ordenado. Esto reduce el número de pasadas necesarias.

import heapq

def balanced_multiway_merge(input_files, output_file):
    # Fusiona varios archivos ordenados en uno solo usando un heap (cola de prioridad)
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
    
    # Cerramos todos los archivos
    for f in archivos:
        f.close()

# Nota: Para un ordenamiento externo completo, primero se generan los runs y se distribuyen
# en varios archivos, luego se fusionan usando esta función. El proceso se repite hasta
# que todo el archivo esté ordenado.

# Ejemplo de uso:
# balanced_multiway_merge(['run0.txt', 'run1.txt', 'run2.txt'], 'salida.txt')