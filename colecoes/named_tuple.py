"""

Named Tuple -> Sao tuplas diferenciadas onde especificmos um nome para mesma e parametros

"""

from collections import namedtuple

# Precisamos definir nome e paramtros

# forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando
ray = cachorro(idade=2, raca='chow-chow', nome='ray')
print(ray)

# Acessando dados
print(ray[0])
print(ray[1])
print(ray[2])

# forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('chow-chow'))
print(ray.count('chow-chow'))
