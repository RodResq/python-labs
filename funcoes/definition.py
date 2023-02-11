"""

cores = ['verde', 'amarelo', 'azul', 'branco']

# functions built-in
print(cores)
cores.append('roxo')
print(cores)
cores.clear()
print(cores)

curso = 'Programacao em Python'
print(curso)

"""

# DRY - Don`t reapeat yourself - Nao repita o codigo

# Como definir funcoes
"""
def nome_funcao(parametro_de_entrada):
    bloco_da_funcao
"""

# definindo uma funcao


def diz_oi():
    print('oi!')

# Ultilizando funcoes

# for n in range(5):
#     diz_oi()

# Em python podemos criar variaveis  do tipo de uma funcao e executa-la atraves da variavel

oi = diz_oi

oi()
