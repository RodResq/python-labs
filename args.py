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

#   COM VALIDACAO DE TIPOS
    def soma_numeros(*args):
        total = 0
        if type(args) is tuple:
            for numero in args:
                if isinstance(numero, int) or isinstance(numero, float):
                    total = total + numero
        return total

# COM FUNCAO BUILTIN SUM
    def soma_numeros(*args):
        return sum(args)


    def soma_numeros(nome, email, *args):
        return sum(args)



    print(soma_numeros('teste', 'teste@email.com') )
    print(soma_numeros('teste', 'teste@email.com', 1))
    print(soma_numeros('teste', 'teste@email.com', 2, 3))
    print(soma_numeros('teste', 'teste@email.com', 3, 4, 5))
    print(soma_numeros('teste', 'teste@email.com', 5, 6, 7, 8))

    print(soma_numeros('teste', 'teste@email.com', 23.4, 12.5))

#   CASE COM EXEMPLO DE VERFIFICACAO DE STRING NO *ARGS e casefold()
    def verifica_info(*args):
        if 'Teste'.casefold() in args or 'Python'.casefold() in args:
        return 'Bem Vindo!'
    return 'Nao passou no teste!'

print(verifica_info())
print(verifica_info('teste'))
print(verifica_info(1, 'python', 3.45))

    # EXEMPLO DE DESEMPACOTOMANTO DE UM ARRAY (VETOR)
    def soma_numeros(*args):
        return sum(args)

    # numeros = [1, 2, 3, 4, 5, 6, 7, 8];
    num_t = [1, 2, 3]
    num1, num2, num3 = num_t
    print(soma_numeros(num1, num2, num3))


    # DESEMPACOTAMENTO COM * (ASTERISCO)
    numeros = [1, 2, 3, 4, 5, 6, 7, 8];
    print(soma_numeros(*numeros))

"""


from ast import arg
from numpy import number

def soma_numeros(*args):
    return sum(args)

numeros = (1, 2, 3, 4, 5, 6, 7, 8);
print(soma_numeros(*numeros))
