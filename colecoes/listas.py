"""

listas: sao representadas por []

lista4 = list(range(11))

num = 18
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Nao encontrei o numero {num}')

lista1.sort()
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Nao encontrei a lista')

lista1.extend([123, 55, 49])
print(lista1)

print(lista1)
lista1.insert(2, 'Geek')
print(lista1)

# lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

lista1.reverse()
print(lista1)
# print(lista1[::-1])
lista2.reverse()
print(lista2)
# print(lista2[::-1])

lista6 = lista2.copy()
print(lista6)

# conta quantidade de elementos
print(len(lista2))

lista5.pop()
print(lista5)

print(lista5.pop(2))
print(lista5)

print(lista5)
lista5.clear()
print(lista5)

# Podemos converter um string em uma lista com o metodo split()
# obs: Por padrao o split() separa os elemento da string por espaco
curso = 'Curso de Programacao em Python'
print(curso)
curso = curso.split()
print(curso)

curso = 'Programacao,em,Python:,avancado'
print(curso)
curso = curso.split(',')
print(curso)


# COloaca em espaco em cada elemento e transforma em uma strinfg

lista6 = ['Programacao', 'em', 'Python:', 'essencial']
print(lista6)

curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# qualquer tipo de dado em uma lista
lista6 = [1, 2.33, 'Geek', True, 'd', [1, 2, 3], 4513213]
print(lista6)

for elemento in lista2:
    print(elemento)

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

print(type([]))


# Ultilizando variaveis em listas

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = list('Geek University')
lista4 = list(range(1, 11))
lista5 = list('Geek University')

# Fazendo acesso a elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']

# print(cores[0])
# print(cores[1])
# print(cores[2])
# print(cores[3])

# Fazendo acesso aos elementos de forma indexida reversa
# print(cores[-1])
# print(cores[-2])
# print(cores[-3])
# print(cores[-4])
# print(cores[-5])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
print(indice, cor)

numeros = [5, 6, 7, 5, 8, 9, 10]

# print(numeros.index(6))
# print(numeros.index(9))

# Fazendo busca a partir de um range com indice inicial e final
print(numeros.index(5, 3, 6))

# Revisao Slice
lista = [1, 2, 3, 4]

# print(lista[1:]) # comecando pelo indice 1
# print(lista[::]) # pegando todos os elemenos
# print(lista[:4])

# print(lista[1:3])

# especificando so passos no slice
# print(lista[1::2])
print(lista[:3:2])

print(lista[::-1])

# Invertendo valores

nomes = ['Geek', 'University']

# nomes[0], nomes[1] = nomes[1], nomes[0]
#
# print(nomes)

nomes.reverse()
print(nomes)


lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

lista = [1, 2, 3, 4, 5, 6]

print(lista)
print(type(lista))


tupla = tuple(lista)
print(tupla)
print(type(tupla))


# desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)
nova.append(4)

print(lista)
print(nova)

# Lista.copy(), listas independentes (Deep Copy)

"""


# Forma 2, modificacao repetida em ambas (Shallow copy)

lista = [1, 2, 3]
nova = lista

print(lista)
nova.append(4)
print(lista)
print(nova)

