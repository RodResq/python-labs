"""

Conjuntos

referencia conjuntos da matematica

conjuntos -> Sets -> Sem duplicados -> Nao ordenados -> Nao exite indice


# forma 1
# Nao aceita valores duplicatos
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(s)
print(type(s))

# Forma 2
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

"""

# Nos Set nao existe ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 34, 5]
print(f'Lista: {lista}')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 34, 5)
print(f'Tuplas: {tupla}')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 34, 5], 'dict')
print(f'Dicionario: {dicionario}')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 34, 5}
print(f'conjunto: {conjunto}')

