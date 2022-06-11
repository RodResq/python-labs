"""
**kwargs

1 - Pode ser qualquer nome
2 - E um paramentro
3 - Exige que ultilizames parametros nomeados
4 - Transforma os parametros extras em um dicionario
5 - Paramentro nao e obrigatorio

# EXEMPLO DE **KWARGS RECEBENDO PARAMETROS NOMEADOS E CONVERTENDO ELES PARA UM DICIONARIO
def cores_favoritas(**kwargs):
    print(type(kwargs))
    print(kwargs)

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# EXEMPLO DE UM LACO FOR NO KWARGS RECUPERANDO CHAVE E VALOR
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} e {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
cores_favoritas()
cores_favoritas(teste='teste')

# EXEMPLO DE CONDICIONAIS NO KARGS, COM VERTICACAO DA STR KEY E STR VALUE
def cumprimento_especial(**kwargs):
    if 'teste' in kwargs and kwargs['teste'] == 'Python':
        return 'Passou no primeiro teste...'
    elif 'test' in kwargs:
        return 'Passou no segundo teste ...'
    return 'Nao passou em nenhum teste ...'

print(cumprimento_especial())
print(cumprimento_especial(teste='Python'))
print(cumprimento_especial(teste='oi'))
print(cumprimento_especial(teste='especial'))


# EXEMPLO DE PASSAGEM DE PARAMETROS NA ORDEM CERTA
1 - PARAMETROS OBRIGATORIO
2 - *ARGS
3 - PARAMETROS DEFAULT (NAO OBRIGATORIOS)
4 - **KWARGS
def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
print('*************************')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=False)
print('*************************')
minha_funcao(34, 'Felipe', eu='Nao', voce='vai')
print('*************************')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# DESEMPACOTANDO DICIONARIO COM **
def mostrar_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostrar_nome(**nomes))



"""

from numpy import kaiser

def soma_multiplos(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}


soma_multiplos(*lista)
soma_multiplos(*tupla)
soma_multiplos(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos(**dicionario)
