"""
Erros mais comuns em Python

ATENCAO: É importante prestar atencao e ler as saidas de erros geradas pela execucao do nosso codigo.

Os erros mais comuns:

SyntaxeError => Oocorre quando o python enocntrar um erro de sintaxe. Ou seja, vc esqueveu algo que o python nao reconhece comco parte da linguagem

a) 
    def funcao:
        print('Geeek Univerite')

b)
    def = 1
    
c) 
    return
    
NameError => Ocorre quando uma variavel ou funcao nao foi definida.
 
Exemplos:
a) print(geek) 
 
b) geek()


TypeError => Ocorre quando uma funcao /operacao /acao é aplicada a um tipo errado.

Exemplos:

a) 
    print(len(5))
    
b) 
    print('geek' + [])

IndexError => Ocorre quando tentando acessar um elemento em um lista ou outro tipo indexado ultilizando um indice invalido.

Exemplo IndexError

a)
    lista = ['Geek']
    print(lista[2])
b)
    lista = ['Geek']
    print(lista[0][4])
c)
    tupla = ['Geek']
    print(tupla[0][4])



ValueError => Ocorre quando uma funcao built-in (integrada) recebe um argumento com o tipo correto mas valor inapropriado.

Exemplos Value Error

a) print(int('Geek'))

KeyError => Ocorre quando tentameos acessar um dicioanrio com uma chave que nao existe

Exemplos KeyError


dic = {}
print(dic['geek'])


AttributeError => Ocorre quando um variavel nao tem uma tributo/funcao.

Exemplos AttributeError:

tupla = (1,43,5,3)
print(tupla.sort())

IdentationError => Occorre quando nao respeitameos a identacao do Python (4 espacos)

"""



















