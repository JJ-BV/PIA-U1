# Problema 1. División de una lista de enteros.
# Escribe una función que reciba por parámetro una lista de enteros y devuelva
# dos listas: una con los valores negavos que tuviera y otra con los posivos.
# Ambas listas deben estar ordenadas ascendentemente

def interger_division(intList):
    positives = []
    negatives = []
    for int in intList:
        if int >= 0:
            positives.append(int)
        else:
            negatives.append(int)
    positives.sort()
    negatives.sort()
    
    print("Positives")
    print(positives)
    print("Negatives")
    print(negatives)

interger_division([1,2,3,4, 0,-5,-6,-7])