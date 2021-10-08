class Restaurante():
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo;

    def descrever_restaurante(self):
        print(f'Nome restaurante e: {self._nome} e tipo: {self._tipo}')

    def descrever_tipo_cozinha(self):
        print(f'Tipo de cozinha e: {self._tipo}')
