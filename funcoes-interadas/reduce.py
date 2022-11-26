"""
Reduce
obs: A partir do python 3+ nao é uma função builtin, ultiliza-lá apartir do módulo functools

Guido van Rossum: Ultilize a função reduce() se relamnete ultilzar ela, na maioria dos casas ultilizar o loop for
"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

mult = lambda x, y: x * y

res = reduce(mult, dados)
print(res)

#Ultilizando um for normal
res = 1
for n in dados:
    res = res * n;
    
print(res);