"""
List Comprehension

1 - Adcionar estruturas condicionais




numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

"""

numeros = [1, 2, 3, 4, 5, 6]
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
