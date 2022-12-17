"""
Len, abs, sum , round

#Len

len() => Retona o tamanho o numero de itens de um iteravel

print(len('Geeel universit'))
print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, toda vez que vc esta ultilizando len o python faz o seguinte:

# Dander len
print('Geek university'.__len__())  # dander é o nome dos 2 tracos


abs() =>  Retorna seu valor absoluto sem o sinal.

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


sum() => Recebe como paramentro um iteravel, podendo receber um valor inicial, e rotorna a soma total dos elementos.
Incluindo o valor inicial

# OBS: O valor inicial default é 0.

# Exemplo

print(sum([1, 2, 3, 4, 5]))     # Lista
print(sum([1, 2, 3, 4, 5], 5))  # Soma com o valor default
print(sum([3.1487, 7.4567]))    # Pontos Flutuantes
print(sum((1, 2, 3, 4, 5)))     # Tupla
print(sum({1, 2, 3, 4, 5}))     # Conjunto ou Set
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))


round() => Retorna um numero arrendodado para n digito de precisao apos a casa decimal. Se a precisao nao for informada,
inteiro mais proximo da entrada

# Exemplo ROund

print(round(3.5))
print(round(3.6))
print(round(3.2121212121, 2))
print(round(3.2399999, 2))
"""







