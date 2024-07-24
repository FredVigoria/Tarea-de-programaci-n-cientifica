# Determinar la relacion de inclusion entre dos conjuntos
# Importamos las librerias propias
import MiLibreria

# Definimos nuestra funcion
def Inclusion(X, Y):
    if MiLibreria.EstaIncluido(X, Y) and MiLibreria.EstaIncluido(Y, X):
        return "Ambos arreglos son iguales"
    elif MiLibreria.EstaIncluido(X, Y):
        return "X esta incluido en Y"
    elif MiLibreria.EstaIncluido(Y, X):
        return "Y esta incluido en X"
    else:
        return "No hay inclusion"

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Insertar N: ",0,9999)
X = MiLibreria.LeerLista("Insertar X: ", N)
M = MiLibreria.LeerEntero("Insertar M: ",0,9999)
Y = MiLibreria.LeerLista("Insertar Y: ", M)

# Mostrar los resultados
print("Conjunto X: ", X)
print("Conjunto Y: ", Y)
print(Inclusion(X, Y))  