# Programa que elimina los elementos duplicados de una lista
# Importamos nuestra libreria
import MiLibreria

# Definir nuestra funcion
def EliminarDuplicados(A):
    resultado = []
    i = 0
    N = len(A)
    
    while i < N:
        # Usar la función Buscar para verificar si el elemento actual ya está en el arreglo resultado
        if MiLibreria.Buscar(A[i], resultado) == -1:
            resultado.append(A[i])
        
        i += 1
    
    return resultado

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Longitud de la lista: ",1,9999)
A = MiLibreria.LeerLista("Inserte el arreglo: ",N)


print("Arreglo original: ", A)
A_sin_duplicados = EliminarDuplicados(A)
print("Arreglo sin duplicados:", A_sin_duplicados)