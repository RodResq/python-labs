"""

Modulo Collections - Default Dict

# Recaptulando dicionarios
dicionario = { 'curso': 'Programacao em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # KeyError

Defult Dict -> Informamos um valor default caso a chave nao exista

"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programacao em python'
print(dicionario)

print(dicionario['outro'])# em um dicionario comum daria keyError

print(dicionario)
