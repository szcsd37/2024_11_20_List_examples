"""
Hozz létre egy listát számokkal, ahol előfordulhatnak duplikációk: [1, 2, 2, 3, 3, 4, 5, 5].
Távolítsd el a duplikált számokat, és írd ki az eredményt!
"""

lista = [1, 2, 2, 3, 3, 4, 5, 5]

nem_setes = []
for num in lista:
    if num not in nem_setes:
        nem_setes.append(num)

print(f"Nem set-es megoldás: {nem_setes}")

# set-es megoldás
setes = list(set(lista))
print(f"Set-es megoldás: {setes}")