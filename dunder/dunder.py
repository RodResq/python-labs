"""

Dunder name e Dunder Main

Dunder Name -> __name__

Dander Main -> __main__

Em python , sao ultilzados dunder para criar funcoes, atrivuots, propriedade e etc, ultilizando Double under para não gerar conflito com os nomes desses elementos na programação.


#Na linguagem C, temos um programa da seguinte forma:

int main() {
    return 0;
}

#Na linguagem java temos:

public static void main(String[] args) {
    
}


# Em paython, se executarmos um modulos python diretamente na linha de comando, internamente o
# python atribuirá a varivel dunder __name__ o valor __main__ indicano que este modulo de execucao é o principal

"""

from funcoes import funcoes_com_parametros

print(funcoes_com_parametros([1, 2, 3, 4, 5]))



