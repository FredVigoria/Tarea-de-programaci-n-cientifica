# Programa que evalua un polinomio en un determinado X
# Importamos nuestra libreria
import MiLibreria

# Definimos nuestra funcion
def EvaluarPolinomio(coeficientes, X):
    N = len(coeficientes)
    resultado = 0
    i = 1
    
    while i <= N:
        # Calcular el valor del termino actual
        termino = coeficientes[N-i] * (X ** i)
        # Sumar el termino al resultado
        resultado += termino
        i += 1
    
    return resultado

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Grado del polinomio: ",1,9999)
coeficientes = MiLibreria.LeerLista("Inserte la lista: ",N+1)
X = MiLibreria.LeerReal("Valor de X: ",1,9999)

# Mostrar resultado
MiLibreria.ImprimirPolinomio(coeficientes,"P")
valor_polinomio = EvaluarPolinomio(coeficientes, X)

print("P(", X, ") = ", valor_polinomio)