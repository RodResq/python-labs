"""
List Comprehension

1 - Pode gerar novas listas a partir de interaveis


[ dado for dado in iteravel ]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

numeros = [1, 2, 3, 4, 5]
res = [numero / 2 for numero in numeros]
print(res)


def eleva_quadrado(num):
    return num * num

res = [eleva_quadrado(numero) for numero in numeros]
print(res)

numeros = [1, 2, 3, 4, 5]

print([numero * 2 for numero in numeros])

"""

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([str(amigo).title() for amigo in amigos])

print([numero * 3 for numero in range(1, 10)])

