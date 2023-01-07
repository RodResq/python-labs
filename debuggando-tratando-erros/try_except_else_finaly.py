"""
Try/ Except / Else / Finaly

obs: TOda entrada deve ser tratada!
OBS: A funcao do usuario é destruir seu sistema.

"""
#else: É executado somente se nao ocorrer um error
#finally: É executado independente de dar error ou nao, é ultilizado para liberar recursos


num = 0
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Voce digitou {num}')
finally:
    print('Excutando o finally')