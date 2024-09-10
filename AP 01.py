lista = [0, 1, 2, 654, 98, 44, 11, 97, 12, 19, 22, 15]
pares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
        pares.sort()
print(pares)