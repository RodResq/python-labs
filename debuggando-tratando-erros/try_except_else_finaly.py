"""
Try/ Except / Else / Finaly

obs: TOda entrada deve ser tratada!
OBS: A funcao do usuario é destruir seu sistema.

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
    
# Generico
def dividir(a, b):
    try:
        ret = int(a) / int(b)
    except ValueError:
        return 'Valor incorreto!'
    except ZeroDivisionError:
        return 'Nao pode dividir por zero!'
    else:
        return ret
    
a = input('Entre com o primeiro numero: ')
b = input('Entre com o segundo numero: ')

print(dividir(a, b))

"""

# Semi-Generico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um error: {err}! '

a = input('Entre com o primeiro numero: ')
b = input('Entre com o segundo numero: ')

print(dividir(a, b))