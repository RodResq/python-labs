"""
    Generators Expression:
    
    em aulas passadas vimos:
    1 - List Comprehension
    2 - Dictionary Comprehension
    3 - Set Comprehension
    
Nao Vimos:
 - Tuple Comprehension....porque elas se chamam generrators
 - o Genrator object é um iteravel

Exemplo List Comprehension, repare os colchetes envolvendo a estrutura
nomes = ['Carlos', 'Camila', 'Carla', 'Criatina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

#  Exemplo Generators:
nomes = ['Carlos', 'Camila', 'Carla', 'Criatina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))


# Biblioteca sys, metodo getsizeof() => Retorna a quantidade de memoria em bytes passada como parametro
from sys import getsizeof

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(976132165464))
print(getsizeof(True))

from sys import getsizeof

# Gerando uma lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando um Set de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

#Gerando um Dictionary de numeros com Dictionary comprehension
dic_comp = getsizeof({ x * 10 for x in range(1000)})

#Gerando um gernarator com Generator expresion 
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa, gastamos em memoria')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

"""

#Interacao no Generator Expression
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)





