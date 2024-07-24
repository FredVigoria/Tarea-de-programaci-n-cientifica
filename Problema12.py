# Programa que reordena descendentemente una lista ascendente
# Importar nuestra libreria
import MiLibreria

# Definimos la funcion de reordenar
def GenerarDescendente(A):
    N = len(A)
    B = [0] * N
    
    i = N - 1
    j = 0
    while i >= 0:
        B[j] = A[i]
        i -= 1
        j += 1
    
    return B

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Longitud de la lista: ",1,9999)
A = MiLibreria.LeerLista("Inserte la lista: ",N)

# Mostrar los resultados
print("Arreglo A (ascendente):", A)
B = GenerarDescendente(A)
print("Arreglo B (descendente):", B)