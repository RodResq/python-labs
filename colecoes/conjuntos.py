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


# removendo elemento

s = {1, 2, 3}

# Forma 1

s.remove(3)

# keyError
# s.remove(33)

print(s)

# forma 2

s = {1, 2, 3}
# Se o valor nao for enconrado nenhum error e gerado
s.discard(22)

print(s)

print(s)
# forma 1 - deep copy
novo = s.copy()
novo.add(4)

print(novo)
print(s)

# Copiando um conjunto para o outro

s = {1, 2, 3}

# forma 2 - shallow copy

novo = s

novo.add(4)

print(novo)
print(s)


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# uniao entre conjuntos - union()
uniao = estudantes_python.union(estudantes_java)
print(uniao)

# Forma 2 - Utilizando o caractere pipe |
uniao2 = estudantes_python | estudantes_java
print(uniao2)
print(type(uniao2))


# forma 1 - Ultilizando o intersection9intersecao)
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# forma 2 - ultilizando o & comercial
ambos2 = estudantes_python & estudantes_java
print(ambos2)

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Metodo de conjunto em python

