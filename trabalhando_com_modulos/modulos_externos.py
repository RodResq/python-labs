"""
Modulos Externos

Ultilizamos o gerenciador de pacotes chamado Pip -> Python Installer Package

colorama -> É ultilizado para permitir impressao de textos no coloral

from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.RED + "geek univerty");
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
print('\033[31m' + 'some red text')
print('\033[39m')


"""
import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)