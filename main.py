from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        sobrenome = input("Digite seu sobrenome: ")
        usuario = Usuario(nome, idade, sobrenome)

        lista_usuarios.append(usuario)

        if idade == 99:
            break

        if idade == 98:
            continue

        print(f"Ola, {usuario.nome} {usuario.sobrenome}, sua idade e {usuario.idade}")

        if usuario.idade <= 17:
            print(f"{usuario.nome} e adolescente")
        elif usuario.idade >= 18 and usuario.idade <= 50:
            print(f"{usuario.nome} e adulto")
        else:
            print(f"{usuario.nome} e idoso")
        continuar = int(input("Deseja continuar cadastrando ? 0 - Sair 1 - Continuar: "))
    except ValueError:
        print("Voce deve informar um numero valido!")
else:
    print("Lista de Usarios cadastrados: ")
    for usuario in lista_usuarios:
        print(f"Nome completo: {usuario.nome} {usuario.sobrenome} - Idade {usuario.idade}")

    print(f"O loop entrou no else")

