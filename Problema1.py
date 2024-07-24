# Determinar si un conjunto esta incluido en otro
# Importamos nuestra libreria
import MiLibreria

# Definimos nuestra funci+on
def EstaIncluido(A, B):
    i = 0
    while i < len(A):
        if MiLibreria.Buscar(A[i], B) ==-1:
            return False
        i += 1
    return True

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Insertar N: ",0,9999)
A = MiLibreria.LeerLista("Insertar los elementos del conjunto A: ", N)
M = MiLibreria.LeerEntero("Insertar M: ",0,9999)
B = MiLibreria.LeerLista("Insertar los elementos del conjunto B: ", M)

# Mostrar los resultados
print("El conjunto A: ", A)
print("El conjunto B: ", B)
print("A esta incluido en B: ",EstaIncluido(A, B))