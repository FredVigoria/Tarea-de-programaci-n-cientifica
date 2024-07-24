# Programa que multilica dos polinomios
# Importamos nuestra libreria
import MiLibreria

# Definimos nuestra función
def MultiplicarPolinomios(P, Q):
    # Longitud de los polinomios
    n = len(P)
    m = len(Q)
    
    # Longitud del polinomio resultante
    R = [0] * (n + m - 1)
    
    # Multiplicar termino a termino
    i = 0
    while i < n:
        j = 0
        while j < m:
            R[i + j] += P[i] * Q[j]
            j += 1
        i += 1
    
    return R

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Inserte el grado del primer polinomio: ",1,99999)
P = MiLibreria.LeerLista("Inserte los coeficientes del primer polinomio: ",N+1)
M = MiLibreria.LeerEntero("Inserte el grado del segundo polinomio: ",1,99999)
Q = MiLibreria.LeerLista("Inserte los coeficientes del segundo polinomio: ",M+1)

# Mostrar resultados
MiLibreria.ImprimirPolinomio(P,"P")
MiLibreria.ImprimirPolinomio(Q,"Q")
MiLibreria.ImprimirPolinomio(MultiplicarPolinomios(P, Q),"(P*Q)") 