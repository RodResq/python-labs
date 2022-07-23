"""
Map 

Com map, fazemos mapeamento de valores para função

# for comun
areas = []
for r in raios:
    areas.append((area(r)))
    
print(areas)

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))


import math


def area(r):
    # Calcula a área de circulo com raio 'r'
    return math.pi * (r * 2)

# print(area(2))
# print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]


# Map com lambdas
areas = map(lambda r: math.pi * (r ** 2), raios)

print(areas)
print(type(areas))
print(list(areas))

"""


#  Ultizamos map onde irá "mapear" cada elemente de dados e aplicar a função.

# exemplo recebendo um lista de tuplas (chave, valor)

cidades_temp = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 29)]
print(cidades_temp)

# f = 9/5 * c + 32

celsios_tofaheint = lambda dado: (dado[0], str(round(9/5, 2) * dado[1] + 32) + ' ©')

print(list(map(celsios_tofaheint, cidades_temp)))