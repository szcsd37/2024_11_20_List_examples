"""
Hozz létre egy listát számokkal: [10, 20, 5, 8, 15].
Írd ki a legnagyobb számot a listából!
"""
lista = [10, 20, 5, 8, 15]

legnagyobb_szam = lista[0]

for num in lista:
    if num > legnagyobb_szam:
        legnagyobb_szam = num
print(f"Nem max függvénnyel: {legnagyobb_szam}")


# max függvény 
legnagyobb = max(lista)
print(f"Max függvénnyel: {legnagyobb}")