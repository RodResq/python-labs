"""
Modulo Collections - Counter

Counter -> Recebe um iteravel e cria um objeto do tipo Collection Counter, que e parecido
com um dicionarios, tendo como chave o elemento e como valor a quantidade de ocorrencia desse elemento


# Podemos ultilizar qualquer iteravel, exemplo de list
lista = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 44, 44, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 66 , 66, 7, 8]

# utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

print(Counter('Geek university'))
# {'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'u': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

"""

# Relaizando o import
from collections import Counter

texto = """partir do romance homônimo escrito por Eiko Kadono, em 1985. Na trama, a jovem bruxa, Kiki, sai de casa 
aos treze anos para tornar-se independente em uma nova cidade, e devido a sua habilidade de voar cria um serviço de 
entregas. Apesar de que a personagem seja uma bruxa, o longa-metragem focaliza nas provações e tribulações de sua 
adolescência. De acordo com Miyazaki, a produção retrata o abismo entre a independência e a confiança nas 
adolescentes nipônicas. O elenco da película é composto pelas vozes de Minami Takayama, Rei Sakuma, Keiko Toda, 
Minami Takayama, Kappei Yamaguchi, entre outros. """

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
# print(res)

# Encontrando as 5 palavras com ocorrencia no texto
print(res.most_common(10))
