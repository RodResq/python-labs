"""

Tuplas (tuple)

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Tupla sao definidas por virgula e nao paratenses
tupla3 = (3, )
print(tupla3)
print(type(tupla3))

tupla4 = 4,
print(tupla4)
print(type(tupla4))

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programacao em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))


"""

# Dicas de ultilizacoa de tupla, ultilizamas tupllas sempre que nao precizarmos alterar seus valores (constante)

meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho')

print(meses)

# acesso de elementos

print(meses[5])

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

