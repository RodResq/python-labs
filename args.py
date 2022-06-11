"""
    Entendendo o * args

    1 - Paramentro como outro qualquer.
    2 - Deve comecar com * (asteriscos)
    3 - Ultilizado em funcao
    4 - Coloca os valores extras em uma tupla
    5 - Sao imutaveis

    def soma_numeros(*args):
        total = 0
    for numero in args:
        total = total + numero
    return total

    def soma_numeros(*args):
        return sum(args)

"""


def soma_numeros(*args):
    return sum(args)

print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(2, 3))
print(soma_numeros(3, 4, 5))
print(soma_numeros(5, 6, 7, 8))