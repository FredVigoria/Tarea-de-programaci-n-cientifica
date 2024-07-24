# Verificar si un conjunto esta ordenado ascendentemente
# Importamos nuestra libreria
import MiLibreria

# Definimos nuestra funcion
def EstaOrdenadoAscendente(A):
    i = 0
    N = len(A)
    while i < N - 1:
        if A[i] > A[i + 1]:
            return False
        i += 1
    return True

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Insertar N: ",1,9999)
A = MiLibreria.LeerLista("Insertar A: ", N)

# Mostrar resultados
print("El conjunto A: ", A)
print("El conjunto A se encuentra ordenado ascendentemente: ",EstaOrdenadoAscendente(A)) 