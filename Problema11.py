# Programa que cuenta las apariciones de un elemento en una lista
# Importar nuestra libreria
import MiLibreria

# Definir la funcion
def ContarApariciones(A, X):
    N = len(A)
    contador = 0
    i = 0
    while i < N:
        if A[i] == X:
            contador += 1
        i += 1
    return contador

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Longitud de la lista: ",1,9999)
A = MiLibreria.LeerLista("Inserte la lista: ",N)
X = MiLibreria.LeerEntero("Inserte el numero a buscar: ",-999999,99999)

# Mostrar resultados
print("Arreglo: ", A)
print("Elemento a contar: ", X)
print("Numero de apariciones de X en el arreglo: ", ContarApariciones(A, X))