# Calcular el producto entre un escalar y un vector
# Importar nuestra libreria
import MiLibreria

# Definimos nuestra funcon
def MultiplicarEscalarPorVector(escalar, vector):
    N = len(vector)
    
    # Crear un nuevo vector para almacenar el resultado
    resultado = [0] * N
    
    # Calcular el producto
    i = 0
    while i < N:
        resultado[i] = escalar * vector[i]
        i += 1
    
    return resultado

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Dimension del vector: ",1,9999)
vector = MiLibreria.LeerLista("Inserte las componentes del vector: ",N)
escalar = MiLibreria.LeerReal("Inserte el escalar: ",-999999,99999)

# Mostrar resultados
print("Vector original: ", vector)
print("Escalar: ", escalar)
vector_multiplicado = MultiplicarEscalarPorVector(escalar, vector)
print("Vector despues de multiplicar por el escalar: ", vector_multiplicado)