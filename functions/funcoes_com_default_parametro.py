"""

Funcoes onde a passagem de parametro seja opcional


def exponencial(numero, potencia=2):
    return numero ** potencia


#  Em funcoes Python, os paramentros com valores default (padrao) DEVEM sempre estar ao final da declaracao
def teste(potencia, num=2):
    return num ** potencia

print(exponencial(2, 3))

print(exponencial(3, 2))

print(exponencial(3))

def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())

def mostrar_informacoes(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem Vindo Instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que era instrutor'
    return f'Ola {nome}'


print(mostrar_informacoes())
print(mostrar_informacoes(instrutor=True))
print(mostrar_informacoes(True)) #Atribuiu ao primeiro paramentro
print(mostrar_informacoes(nome='Stephany'))


# Pasando funoes como parametro

def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo

# Variaveis Globais
# Variaveis Locais

instrutor = 'Geek'


def diz_oi():
    instrutor = 'Python'
    return f'Oi {instrutor}'


print(diz_oi())

total = 0

def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador

    return dentro()


print(fora())
print(fora())
print(fora())


# Quais tipos de dados podemos ultilaicar como valores default de aramenttros
    - Number, strings , floats , booleanos, listas, tuplasm dicionarios, funcoes e etc


# Passando funcoes como paramentro


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e confusoes

# Variaveis Globais

instrutor = 'Geek'


def diz_oi():
    instrutor = 'Python' # variavel Local
    return f'oi {instrutor}'


print(diz_oi())

# OBS: A variavel local tem preferencia da variavel global, na hipotese de ultilizarem o mesmo nome

#  Atencao com variaveis gloabais, se possivel evitar


"""

# Ultilizando a variavel global em um escopo local

total = 1 # variavel global


def incrementa():
    global total # Usar a palavra chave 'global'
    total = total + 1
    return total


print(incrementa())







