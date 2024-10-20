# Problema 3. Intersección y unión de conjuntos
# Escribe un programa que permita al usuario crear dos conjuntos de números
# enteros. Luego, el programa debe calcular y mostrar:
# 1. La intersección de ambos conjuntos (elementos comunes).
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto,
# pero no en ambos).



def set_creator(orderNumber):
    print("Set : " + str(orderNumber))
    numberSet = set()
    while True:
        try:
            inputNumber = int(input("Write any number or press any key to exit: "))
            numberSet.add(inputNumber)
        except ValueError:
            break
    return numberSet

set1 = set_creator(1)
set2 = set_creator(2)

print("Set 1: ", set1)
print("Set 2: ", set2)

intersection = set1.intersection(set2)
print("Intersection: ", intersection)

union = set1.union(set2)
print("Union: " + str(union))

simetricDif = set1.symmetric_difference(set2)
simetricDif1 = set1.difference(set2)
simetricDif2 = set2.difference(set1)
print("Simetric difference (set1 - set2): ", simetricDif1)
print("Simetric difference (set2 - set1): ", simetricDif2)
print("Simetric difference: ", simetricDif)
