"""
Sorted: serve para orddenar elementos

Obs: Não confunidr com a funcao sort() estuda em listas. O sort() so funciona em listas.


Podemos ultizar o sorted() com qualquer iteravel

obs:  O soted() sempre retorna uma lista

# O sorted() mantem a lista original inalterado, diferente do metodo sort()
numeros = {6, 1, 8, 2}

print(numeros)

print(sorted(numeros))

print(numeros)

# Adicionando paramentos ao sorted

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros, reverse=True))
print(numeros)

#Trabalhando com sorted para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"},
]  

print(usuarios)
#Ordenando pelos nomes dos usuarios - Ordem Alfabetica
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=False))

#Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

"""
musicas = [
    {'titulo': 'a', 'tocou': 7},
    {'titulo': 'b', 'tocou': 4},
    {'titulo': 'c', 'tocou': 3},
    {'titulo': 'd', 'tocou': 32}
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
