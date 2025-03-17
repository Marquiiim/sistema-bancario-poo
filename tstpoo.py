class Pessoa:
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._nascimento
    
pessoa = Pessoa("Marcos", 2006)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")