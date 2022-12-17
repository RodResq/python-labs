"""
min e max

max() => retorna o valor de um interavel ou o maior valor de dois ou mais elementos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))

print(max(3, 34))

val1 = int(input('Informe o valor 1: '))
val2 = int(input('Informe o valor 2: '))

print(max(val1, val2))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c'))

print(max(3.45345, 5.65776))

print(max('Geek University'))


#################################

min() => Retorna o menor valor em um interavel ou o menor de dois ou mais elementos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

print(min(3, 34))

val1 = int(input('Informe o valor 1: '))
val2 = int(input('Informe o valor 2: '))

print(min(val1, val2))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c'))

print(min(3.45345, 5.65776))

print(min('Geek University'))


nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']
print(max(nomes))   # Tim
print(min(nomes))   # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Olivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim

# Verificando min im max de uma lista de dictionary
musicas = [
    {'titulo': 'a', 'tocou': 7},
    {'titulo': 'b', 'tocou': 4},
    {'titulo': 'c', 'tocou': 3},
    {'titulo': 'd', 'tocou': 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))
"""
# Outros Exemplos

musicas = [
    {'titulo': 'a', 'tocou': 7},
    {'titulo': 'b', 'tocou': 4},
    {'titulo': 'c', 'tocou': 3},
    {'titulo': 'd', 'tocou': 32}
]

print(dict(max(musicas, key=lambda musica: musica['tocou'])).get('titulo'))
print(dict(min(musicas, key=lambda musica: musica['tocou'])).get('titulo'))

# DESAFIO! Como criar a musica mais tocada e menos tocada sem usar max(), min() e lambda?

mais_tocada = 0
for musica in musicas:
    if musica['tocou'] > mais_tocada:
        mais_tocada = musica['tocou']

for musica in musicas:
    if musica['tocou'] == mais_tocada:
        print(musica['tocou'])


menos_tocada = 9999
for musica in musicas:
    if musica['tocou'] < menos_tocada:
        menos_tocada = musica['tocou']

for musica in musicas:
    if musica['tocou'] == menos_tocada:
        print(musica['tocou'])


