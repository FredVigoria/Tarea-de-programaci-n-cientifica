def LeerEntero(texto,menor,mayor):
    n = int(input(texto))
    while (not menor<=n) and (not n<=mayor):
        n = int(input(texto))
    return n

def LeerReal(texto,menor,mayor):
    n = float(input(texto))
    while (not menor<=n) and (not n<=mayor):
        n = float(input(texto))
    return n

def LeerLista(texto,Longitud):
    k = 0
    l = []
    print(texto)
    while k < Longitud:
        l.append(float(input(f"Elemento {k+1}: ")))
        k += 1
    return l

def EstaIncluido(A, B):
    i = 0
    while i < len(A):
        if Buscar(A[i], B) ==-1:
            return False
        i += 1
    return True

def Buscar(x, C):
    L = len(C)
    k = 0
    while k < L:
        if C[k] == x:
            return k
        k += 1
    return -1

def ImprimirPolinomio(Coeficientes, nombre):
    t = f"{nombre}(x) = "
    i = 0
    while i < len(Coeficientes):
        if Coeficientes[i] == 0:
            pass
        elif len(Coeficientes)-i-1 == 1:
            t += str(Coeficientes[i])+"x"+" + "
        elif len(Coeficientes)-i-1 == 0:
            t += str(Coeficientes[i])
        else:
            t += str(Coeficientes[i])+"x^"+str(len(Coeficientes)-i-1)+" + "
        i += 1
    print(t)

