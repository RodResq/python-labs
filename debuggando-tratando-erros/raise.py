"""_summary_
Levantand os proprios errors com o raise

raise -> Lanca excessoes

OBS: O raise nao é uma funcção, é uma palavra reservada com def ou outra qualquer em python

Ultilizando para criar nossa proprias excessoes e msg de erros

A forma de ultilizacao é:

raise TipoError('Messagem error')
    

#Exemplo Real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor deve ser uma string')
    print(f'O texto {texto} sera impresso na cor: {cor}')
    
colore(True, "Azul")
    
    
OBS: o RAISE igual ao RETURN finaliza a funcao, nada é executado depois!
"""
# raise ValueError('Valor incoreto');

#Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor deve ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} sera impresso na cor: {cor}')
    
colore('True', "cinza")
