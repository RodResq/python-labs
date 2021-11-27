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

"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando Valores
# Forma 1
print(paises['br'])
# print(paises['ru'])

# keyError -> quando chave nao existe

# FOrma 2 - Acessenado via get
# Acessando via get
print(paises.get('br'))
print(paises.get('ru'))
