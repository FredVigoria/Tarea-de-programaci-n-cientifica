# Sumar dos polinomios 
# Importamos nuestra libreria
import MiLibreria

# Definimos la funcion de sumar polinomios
def SumarPolinomios(P, Q):

    # Longitud del polinomio resultante
    max_len = max(len(P),len(Q))
    
    # Inicializar el polinomio suma con ceros
    S = [0] * max_len
    
    # Completar con ceros para que tengan la misma longitud
    while len(P) < max_len:
        P = [0] + P
    while len(Q) < max_len:
        Q = [0] + Q

    # Sumar termino a termino 
    i = 0
    while i < max_len:
        S[i] = P[i] + Q[i]
        i += 1
    # Devolver el polinomio suma
    return S

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Inserte el grado del primer polinomio: ",1,99999)
P = MiLibreria.LeerLista("Inserte los coeficientes del primer polinomio: ",N+1)
M = MiLibreria.LeerEntero("Inserte el grado del segundo polinomio: ",1,99999)
Q = MiLibreria.LeerLista("Inserte los coeficientes del segundo polinomio: ",M+1)

# Mostrar los resultados
MiLibreria.ImprimirPolinomio(P,"P")
MiLibreria.ImprimirPolinomio(Q,"Q")
MiLibreria.ImprimirPolinomio(SumarPolinomios(P, Q),"(P+Q)")