# Programa que calcula los promedios finales
# Importamos nuestra libreria
import MiLibreria

# Definimos las funciones
def CalcularPromediosFinales(parcial1, parcial2, parcial3, sustitutorio):
    N = len(parcial1)
    promedios_finales = [0] * N
    
    i = 0
    while i < N:
        # Encontrar el minimo entre los tres parciales
        min_parcial = min(parcial1[i], parcial2[i], parcial3[i])
        
        # Determinar si el sustitutorio reemplaza al minimo
        if sustitutorio[i] > min_parcial:
            if min_parcial == parcial1[i]:
                parcial1[i] = sustitutorio[i]
            elif min_parcial == parcial2[i]:
                parcial2[i] = sustitutorio[i]
            else:
                parcial3[i] = sustitutorio[i]
        
        # Calcular el promedio final
        promedio = (parcial1[i] + parcial2[i] + parcial3[i]) / 3
        promedios_finales[i] = promedio
        
        i += 1
    
    return promedios_finales

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Numero de alumnos: ",1,9999)
parcial1 = MiLibreria.LeerLista("Inserte las notas del parcial 1: ",N)
parcial2 = MiLibreria.LeerLista("Inserte las notas del parcial 2: ",N)
parcial3 = MiLibreria.LeerLista("Inserte las notas del parcial 3: ",N)

sustitutorio = MiLibreria.LeerLista("Inserte las notas del sustitutorio: ",N)

# Mostrar los resultados
print("Notas del primer parcial: ", parcial1)
print("Notas del segundo parcial: ", parcial2)
print("Notas del tercer parcial: ", parcial3)
print("Notas del sustitutorio: ", sustitutorio)

promedios_finales = CalcularPromediosFinales(parcial1, parcial2, parcial3, sustitutorio)

print("Promedios finales: ", promedios_finales)