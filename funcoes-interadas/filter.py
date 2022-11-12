"""
Filter -> serve para filtrar dados de um determinada colecao
"""  
# Bibliotesa
import statistics
# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1, -0.1]

media = statistics.mean(dados)
# print(media)

# Obs: Assim como a funcao map(), a filter recebe dois parametros, sendo uma funcao e um interavel
res = filter(lambda valor: valor > media, dados)
print(list(res))
    
    
    
    