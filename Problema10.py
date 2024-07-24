# Calcular el producto escalar entre dos vectores
# Imprimir la libreria
import MiLibreria

# Definimos la funcion de producto escalar
def ProductoEscalar(A, B):
    N = len(A)
    
    # Inicializar el producto escalar
    producto = 0
    
    # Calcular el producto escalar
    i = 0
    while i < N:
        producto += A[i] * B[i]
        i += 1
    
    return producto

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Dimension de los vectores: ",1,9999)
A = MiLibreria.LeerLista("Inserte las componentes del vector A: ",N)
B = MiLibreria.LeerLista("Inserte las componentes del vector B: ",N)

# Mostrar los resultados
print("Vector A:", A)
print("Vector B:", B)
print("Producto escalar:", ProductoEscalar(A, B))