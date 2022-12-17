"""
Reversed

OBS: Nao confunda com a versao reverse() que estudamos nas listas

A funcao reverse() so funciona em lista ja a funcao reversed() funciona em qualquer iteravel

A funcao reversd() retorna um iteravel do tipo list_reverseiterator
"""

# Exemplo

lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(type(res))

# convertendo para um iteravel
# Lista
print(list(reversed(lista)))
# Tupla
print(tuple(reversed(lista)))

# Em conjuntos nao definimos a ordem dos elementos
# Conjunto(set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')
print('\n')

# Podemos fazer sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Fazend com o slice de string
print('Geek University'[::-1])

# Podemos ultilizar o reversed para fazer o loop reverso
for n in reversed(range(0, 10)):
    print(n)

# ultilizando o proprio range
for n in range(9, -1, -1):
    print(n)
