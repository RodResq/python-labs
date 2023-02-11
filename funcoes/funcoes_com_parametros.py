"""

Funcoes com parametros

Recebem dados para serem processadas dentro da mesma

# Funcoes podem ter n paramtroes de entrada

def soma(a, b):
    return a + b;


def multiplica(a, b):
    return a * b


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'University '))

def nome_completo(nome, sobrenome):
    return f'Seu nome completo e {nome} {sobrenome}'

# print(nome_completo('Angelina', 'Jolie'))
nome = 'Angelina'
sobrenome = 'Jolie'

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome=sobrenome, nome=nome))

"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
else:
    print(f'O mudulo funcoes com paramentrs foi importado {__name__}')
















