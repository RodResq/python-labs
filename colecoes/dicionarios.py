"""

Dicionarios

Em algumas lingguagem de programacao os dicionariros sao conhecidos por mapas.

Dicionarios sao colecoes de tipo chave/valor

Dicionarios sao representados por chaves {}.

print(type({}))
    - Chave e valor soa separados dois pontos: {'chave': 'valor'}
    - podem ser de qualquer tipo
    - podemos misturar tipos

# forma 1 (mais comun)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# forma 2 (menos comun)
paises = dict(br='Braisl', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando Valores
# Forma 1
print(paises['br'])
# print(paises['ru'])

# keyError -> quando chave nao existe

# FOrma 2 - Acessenado via get
# Acessando via get
print(paises.get('br'))
print(paises.get('ru'))

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Nao encontrei o pais')

Podemos definir uma valor padrao, caso nao encontremos o objeto
pais = paises.get('ru', 'Nao encontrado')
print(f'Encontrei o pais {pais}')

# Podemos verficar se determinda chave in dicionario

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

localidades = {
    (35.6895, 396917): 'Escritorio em Toqui',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em Sao Paulo'
}

print(localidades)
print(type(localidades))


# Adcionar Elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1

receita['abril'] = 350
print(receita)

# Forma 2 - Mais Elegante

novo_dado = {'mai': 500}
receita.update(novo_dado) # Outra forma: receita.update({'mai', 500})

print(receita)

# Atualizando Dados em um dicionario:

receita['mai'] = 550
print(receita)

receita.update({'mai': 600})
print(receita)

# Remover dados de um dicionario

# Foma 1 - mais comun
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
ret = receita.pop('mar') # remove e retorna o valor
print(ret)
# informar a chave, se nao encontre -> keyError

print(receita)

# Forma 2

del receita['fev']
print(receita)

# Ulizando Lista
carrinho = []

carrinho1 = ['Playstation', 1, 2300.00]
carrinho2 = ['God of War 4', 1, 150.00]

carrinho.append(carrinho1)
carrinho.append(carrinho2)

print(carrinho)

# Ultilizando Tuplas

produto1 = ('Playstation', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Ultilizando Dicionario

carrinho = []

carrinho1 = {'nome': 'Playstation 4', 'quantidade': 1, 'valor': 2300.00}
carrinho2 = {'nome': 'God of War', 'quantodade': 1, 'valor': 150.00}

carrinho.append(carrinho1)
carrinho.append(carrinho2)
print(type(carrinho))
print(carrinho)


print(d)
print(type(d))

d.clear()

print(d)

# Deep Coopy
novo = d.copy();

# novo.update({'d': 4})
novo['d'] = 4

print(novo)

d = dict(a=1, b=2, c=3)

# Shalow copy
novo = d

novo['d'] = 4

print(novo)
print(d)


"""

# Forma nao usual de criar dictionary

outro = {}.fromkeys('a', 'b')

print(type(outro))
print(outro)

# Outra forma

outro = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(type(outro))
print(outro)

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'valor')
print(veja)


