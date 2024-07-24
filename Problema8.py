# Eliminar un elemento de una lista
# Importar la libreria
import MiLibreria

# Definimos nuestra función
def EliminarElemento(A, X):
    # Buscar el índice del elemento a eliminar usando la función Buscar
    i = MiLibreria.Buscar(X, A)
    
    # Si el elemento fue encontrado
    if i != -1:
        N = len(A)
        # Desplazar elementos hacia la izquierda
        j = i
        while j < N - 1:
            A[j] = A[j + 1]
            j += 1
        # Eliminar el último elemento duplicado
        A.pop()  # Remove the last element which is now a duplicate
    
    return A

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Longitud de la lista: ",1,9999)
A = MiLibreria.LeerLista("Inserte la lista: ",N)
X = MiLibreria.LeerEntero("Inserte el numero a eliminar: ",-999999,99999)

# Mostrar resultados
print("Arreglo original:", A)
A = EliminarElemento(A, X)
print("Arreglo despues de eliminar el elemento:", A)