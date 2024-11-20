"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""

szamok = [5, 8, 12, 15, 22]

szam_index = 1
for szam in szamok:
    print(szam_index)
    szam_index += 1
print()

print(len(szamok))