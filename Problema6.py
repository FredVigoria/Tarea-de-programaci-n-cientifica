# Econtrar la notas mas frecuente de una lista de notas
# Importar nuestra libreria
import MiLibreria

# Definimos nuestra funcion
def NotaMasFrecuente(notas):
    notas_unicas = []
    frecuencias = []
    i = 0
    while i < len(notas):
        nota = notas[i]
        # Usar la funcion Buscar para verificar si la nota ya esta en notas_unicas
        indice = MiLibreria.Buscar(nota, notas_unicas)
        if indice != -1:
            frecuencias[indice] += 1
        else:
            notas_unicas.append(nota)
            frecuencias.append(1)
        i += 1
    # Encontrar la nota con la mayor frecuencia
    max_freq = -1
    nota_mas_frecuente = None
    k = 0
    while k < len(frecuencias):
        if frecuencias[k] > max_freq:
            max_freq = frecuencias[k]
            nota_mas_frecuente = notas_unicas[k]
        k += 1
    
    return nota_mas_frecuente

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Inserte el numero de notas: ", 1, 99999)
notas = MiLibreria.LeerLista("Inserte las notas: ", N)

# Mostrar los resultados
print(f"La nota que mas se repite es: {NotaMasFrecuente(notas)}")