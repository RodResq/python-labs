"""

[5] - Imports

- Imports devem ser sempre feitos em linhas separadas

# Import Errado:

import sys, os

# Import Certo

import sys
import os

# Nao ha problemas em ultilizar

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer

from types import (
    StryngType,
    ListType,
    SetType,
    OutroType
)

[6] - Espacos em Expressoes e instrucoes

# Nao faca

funcao( algo[ 1 ], { outro: 2 } )
algo (1)

# Faca

funcao(algo[1], {outro: 2})

[7] - Termine sempre um instrucao com uma linha em branco
"""
import this
