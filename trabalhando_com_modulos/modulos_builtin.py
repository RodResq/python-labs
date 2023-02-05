"""
  Trabalhando com Modulos Builtin(Modulos integrados no Python)

______________________
|Python|Mdulos Builtin
----------------------
# ultilizando alias (apelidos) para mdoulos/funcoes

import random as rdm

print(rdm.random())

#Podemos importar todas as funcoes de um modulo ultilizando o *

from random import *

print(random())


#Importndo todo o modulo

import random
print(random.random())

# Ultilizando alias para a funcao
from random import randint as rdi

print(rdi(5, 89))

# Ultilizando alias para a funcao
from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())


"""


#Costumamos ultilizar tuple para colocar multiplos import so mesmo modulo
# from random import random, randint, shuffle, sample, choice

from random import (
    random, 
    randint, 
    shuffle,
    choice,
    sample
)

print(random())
print(randint(1, 54))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice(lista))












