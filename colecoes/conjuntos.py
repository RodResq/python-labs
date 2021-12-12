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

# Nos Set nao existe ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 34, 5]
print(f'Lista: {lista} com {len(lista)} tamanho')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 34, 5)
print(f'Tuplas: {tupla} com {len(tupla)} tamanho')

# Dicionarios nao eaceiram chaves duplicadas
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 34, 5], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} tamanho')

# Conjuntos noao aceitam valores duplicados
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 34, 5}
print(f'conjunto: {conjunto} com {len(conjunto)} tamanho')

# POdemo colocar dados de tipos misturados nos sets
s = {1, 'b', True, 35.22, 44}
print(s)
print(type(s))

# Podemos iterar nos set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets
s = {1, 2, 3}

s.add(4)
s.add(4)
print(s)

"""

# removendo elemento

s = {1, 2, 3}

# Forma 1

s.remove(3)

print(s)

# forma 2

s.remove(33)

print(s)
