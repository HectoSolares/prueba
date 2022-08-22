## Ejercicio 1, obtener el numero mayor
# x e y son números enteros
# Devuelve el número más grande
# Si son iguales, devuelve cualquiera de los dos
# Tu código:

def obtMayor(x,y):
    if x > y:
        print('El numero ' + str(x) + ' es el mayor')
    elif y > x:
        print('El numero ' + str(y) + ' es el mayor')
    else:
        print('Son iguales')

obtMayor(100,1000)

