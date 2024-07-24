# Programa para calcular los precios
# Importar nuestra libreria
import MiLibreria

# Definir nuestra funcion
def CalcularPreciosTotales(unidades_vendidas, precios_unitarios):
    N = len(unidades_vendidas)
    
    precios_totales = [0] * N
    gran_total = 0
    
    i = 0
    while i < N:
        precios_totales[i] = unidades_vendidas[i] * precios_unitarios[i]
        gran_total += precios_totales[i]
        i += 1
    
    return precios_totales, gran_total

# ------------- Ejemplo de uso ------------------
# Leer los datos
N = MiLibreria.LeerEntero("Numero de objetos en venta: ",1,9999)
unidades_vendidas = MiLibreria.LeerLista("Inserte las unidades vendidas: ",N)
precios_unitarios = MiLibreria.LeerLista("Inserte los precios unitarios: ",N)

# Mostrar los resultados

print("Numero de unidades vendidas de articulos: ",unidades_vendidas)
print("Precios unitarios de los articulos: ",precios_unitarios)

precios_totales, gran_total = CalcularPreciosTotales(unidades_vendidas, precios_unitarios)

print("Precios totales de cada articulo:", precios_totales)
print("Gran total de ventas:", gran_total)
