# Programa que inserta un elemento en una lista ordenada
# Importamos nuestra libreria
import MiLibreria

# Definimos nuestra funcion
def InsertarEnArregloOrdenado(A, num):
    N = len(A)
    
    # Encontrar la posicion de insercion
    i = 0
    while i < N and A[i] < num:
        i += 1
    
    # Desplazar elementos para hacer espacio
    A.append(0)  # Anadir un elemento al final para ampliar la lista
    j = N - 1
    while j >= i:
        A[j + 1] = A[j]
        j -= 1
    
    # Insertar el nuevo numero
    A[i] = num
    
    return A

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Longitud de la lista: ",1,9999) 
A = MiLibreria.LeerLista("Inserte la lista: ",N)
X = MiLibreria.LeerReal("Inserte el numero a insertar: ",-999999,99999)

# Mostrar resultados 
print("Arreglo original:", A)
A = InsertarEnArregloOrdenado(A, X)
print("Arreglo despues de la insercion:", A)