"""

Modulo Random e o que sao modulos:

- Modulos em Python nada mais são do que outros arquivos Python.


Módulo arandom: Possui varias funcoes para geracao de numeros pseudo-aleatório.


#OBS: Existem duas formas de se ultilizar um módulo ou funcao deste

#Forma 1 - Importtando todo o módulo (Nao recomendaddo)

import random

# random -> Gera um numero psedudo aleatorio entre 0 e 1.

#Ao realizar o import de todo o módulo, todas as funcoes, atributos, classes e propriedades que estiverem, ficarão em memoria.
#OBS: Caso vc saiba quais funcoes vc precisa ultilizar as funcoes ficaria na forma 2

print(random.random())

#Para ultizar random(), colocamos o nome do pacote e o nome da funcao.

#obs: Nao confundir funcao random com o pacote random. Pode parecer confuso, mas a funcao random é apenas um funcao dentro do modulo random.


#Forma 2 - Iimportando uma funcao especifica do random. Forma recomendada

from random import random

# No import assima, do modulo random import a funcao random.

for i in range(0, 10):
    print(random())



# uniform() -> Gerar um numero pseudo aleatorio entre os valores estabelecidos.

from random import uniform

for i in range(10):
    print(uniform(5, 10)) # 7 nao incluido
    
# Gera um numero real com valores pre estabelecidos.

# randint() -> Gerra valores pseufdo-aleatorio entre os valores estabelecidos.

# Gerador de apostas para a mega-sena

from random import randint

for i in range(6):
    print(randint(1, 61), end=", ")

# choice() -> Mostart um valor aleátorio entre un interavel

from random import choice

jogadores = ['pedra', 'papel', 'tesoura']

print(choice(jogadores))



"""



#shuffle() -> tem a funcao de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'j', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(cartas)

shuffle(cartas)

print(cartas)

