# Método de Ordenamiento Externo: Natural Merging
# -----------------------------------------------
# Natural Merging es una variante del straight merging. En lugar de dividir el archivo
# en bloques de tamaño fijo, detecta secuencias ya ordenadas (runs naturales) en el archivo
# y las fusiona. Esto puede reducir el número de pasadas necesarias si los datos ya tienen
# partes ordenadas.

def detectar_runs(nombre_archivo):
    # Detecta runs naturales en un archivo y los separa en archivos temporales
    runs = []
    with open(nombre_archivo, 'r') as f:
        run = []
        anterior = None
        for linea in f:
            num = int(linea)
            if anterior is not None and num < anterior:
                # Fin de un run, guardamos el actual
                runs.append(run)
                run = []
            run.append(num)
            anterior = num
        if run:
            runs.append(run)
    return runs

def escribir_runs(runs, prefijo='run'):
    # Escribe cada run en un archivo temporal
    archivos = []
    for i, run in enumerate(runs):
        nombre = f"{prefijo}{i}.txt"
        with open(nombre, 'w') as f:
            for num in run:
                f.write(f"{num}\n")
        archivos.append(nombre)
    return archivos

def merge_files(file1, file2, output):
    # Fusiona dos archivos ordenados en uno solo (igual que en straight merging)
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as fout:
        line1 = f1.readline()
        line2 = f2.readline()
        while line1 and line2:
            if int(line1) <= int(line2):
                fout.write(line1)
                line1 = f1.readline()
            else:
                fout.write(line2)
                line2 = f2.readline()
        while line1:
            fout.write(line1)
            line1 = f1.readline()
        while line2:
            fout.write(line2)
            line2 = f2.readline()

# Nota: Para un ordenamiento externo natural completo, se detectan los runs naturales,
# se escriben en archivos temporales y luego se fusionan repetidamente hasta que quede
# un solo archivo ordenado. Este ejemplo muestra cómo detectar runs y fusionar archivos.

# Ejemplo de uso:
# runs = detectar_runs('datos.txt')
# archivos = escribir_runs(runs)
# merge_files(archivos[0], archivos[1], 'salida.txt')