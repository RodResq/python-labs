"""

Conhecidos em python como dicionario
Dicionarios em Python sao representados por chaves {}

# interar sobre dicionarios
# Imprimindo as chaves
for chave in receita:
    print(chave)

# Imprimindo os valores
for chave in receita:
    print(receita[chave])

# Imprimindo chaves e valores:
for chave in receita:
    print(f'chave: {chave}, valor: {receita[chave]}')


# Conhecer todas as chaves
print(receita.keys())

# Podemos iterar sobre as chaves (recomendavel):
for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

# Iterando sobre valores
for valor in receita.values():
    print(valor)

# Desempacotamento de Dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'chave: {chave}, valor: {valor}')

# Soma, valor Maximo, valor Minimo, tamanho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


"""


receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)



