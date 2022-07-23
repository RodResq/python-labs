"""
Map 

Com map, fazemos mapeamento de valores para função
"""

import math


def area(r):
    """Calcula a área de circulo com raio 'r'."""
    return math.pi * (r * 2)

# print(area(2))
# print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# for comun
areas = []
for r in raios:
    areas.append((area(r)))
    
print(areas)

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

