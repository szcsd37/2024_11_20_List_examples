"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""

list1 = [3, 1, 4]
list2 = [9, 7, 2]

lista = list1 + list2

lista.sort()

print(lista)

# írasd ki az első és az utolsó elemet!
print(lista[0])
print(lista[-1])