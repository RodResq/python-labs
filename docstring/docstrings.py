"""
Documentando funcoes com docstring
"""

# Exemplo

# podemos ter acesso a uma documentacao em python atravez de uma propriedade espacial: __doc__

# podemos ainda fazer acesso a documentacao com o help()


def diz_oi():
    """Uma funcao simples que retorna 'Oi!"""
    return 'Oi!'


print(diz_oi())


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de numero ou o numero a potencia informada
    :param numero: Numero que desejameos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial, default 2
    :return: retorna o exponencal de um numero pela potencia
    """
    return numero ** potencia


print(exponencial(2))
