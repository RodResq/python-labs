"""

Ultilizamos o bloco try/cath para tratar error que podem ocorrer no nosso código.
Previnindo assim que o programa para de funcionar eo usuario recebe messagem de error inesperadas.

A forma geral mais simples é:

try:
// Execucao problemenatica
except:
    //o que deve ser feito em caso de problema
    
try:
    geek()
except NameError:
    print('Deu algun error')
    
try:
    len(5)
except TypeError as err:
    print(f'A aplicao gerou o seguinte error: {err}')
    
"""

# Tratando um error generico

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'Geek'}

print(pega_valor(dic, 'key'))