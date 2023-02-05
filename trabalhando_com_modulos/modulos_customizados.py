"""
Modulos Customizados
    
Como modulos python nada maus sao do que arquivos em python, entao todos os arquivos que criamos nesse curso sao modulos python prontos para serem ultilizados.    


#Importando uma funcao especifica do modulo
from funcoes_com_parametros import soma_impares

print(soma_impares([1, 3, 5, 7, 9]))

"""

#Importando todo o modulo (temos acesso a TODOS os elementos do modulo)

import funcoes_com_parametros as fcp

print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))