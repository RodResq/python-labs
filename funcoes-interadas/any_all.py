"""
Any e All

All: Retona True se todos os elementos do iteravel sao verdadeiros ou se o iteravel esta vazio
        
print(all([0, 1, 2, 3, 4])) # Todoos os numeros sao True, exceto o 0
print(all([1, 2, 3, 4])) # Todoos os numeros sao True


print(all((1, 2, 3, 4))) #Tupla
print(all({1, 2, 3, 4})) #Set
print(all('Geek')) #String


nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'aeio' if letra in 'aeiou']))


print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

##############
any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se oiteravel estiver vazio, retorna False

"""

print(any([0, 1, 2, 3, 4]))

print(any([0, False, {}, (), [], '']))