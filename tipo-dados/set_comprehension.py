"""
Set comprehension
obs: Conjunto nao mantem organizacao, e nao aceita repetidos

Set = {1, 2, 3, 4, 5}

"""

numeros = {num for num in range (1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)