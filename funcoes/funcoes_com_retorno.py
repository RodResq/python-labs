"""
Funcao com retorno

numeros = [1, 2, 3]

print(numeros.pop())
print(numeros)

def quadrado_de_sete():
    return 7 * 7

print(quadrado_de_sete())

def nova_funcao():
    variavel = ''
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

from random import random


def jogo_moedo():
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'

"""


def e_impar():
    numero = 5
    if numero % 2 == 0:
        return False
    return True


print(e_impar())
