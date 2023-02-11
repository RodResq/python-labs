"""
    
from geek import geek1, geek2
from geek.university import geek3, geek4


print(geek1.pi)
print(geek1.funcao1(2, 3))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())
    
"""

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4
from funcoes import funcoes_com_parametros


print(funcao1(4, 2))
print(funcao4())
print(funcoes_com_parametros.soma_impares([1, 2, 3]))


