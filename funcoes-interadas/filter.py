"""
Filter -> serve para filtrar dados de um determinada colecao
# Bibliotesa
import statistics
# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1, -0.1]

media = statistics.mean(dados)
# print(media)

# Obs: Assim como a funcao map(), a filter recebe dois parametros, sendo uma funcao e um interavel
res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))
# obs: assim como na funcao map apos serem ultilizados os dados de filter, eles sao excluidos da memoria 
print(f'Novamente: {list(res)}')

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
    
print(paises)

print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)
print(list(res))    


usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]    
# print(usuarios)
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(list(inativos))
"""  
nomes = ['Vanessa', 'Ana', 'Maria']
lista = list(map(lambda nome: f'Sua instrutora e {nome}', filter(lambda nome: len(nome) > 3, nomes)))
print(lista)