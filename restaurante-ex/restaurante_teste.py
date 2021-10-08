from restaurante import Restaurante

restaurante = Restaurante('Meu Restaurante', 'Peixaria')
restaurante.descrever_restaurante()
restaurante.descrever_tipo_cozinha()

print(f"properti nome restaurante = {restaurante.nome}")
print(f"property tipo restaurante {restaurante.tipo}")
