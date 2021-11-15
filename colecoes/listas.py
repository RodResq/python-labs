"""

listas: sao representadas por []
"""

print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))

num = 18
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Nao encontrei o numero {num}')

lista1.sort()
print(lista1)

