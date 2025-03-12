"""
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")

tst1 = Cachorro("Logan", "Capa-preta")

tst1.latir()
"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, nro_marcha=1):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.nro_marcha = nro_marcha

    def buzinar(self):
        print("Plim, plim.")

    def parar(self):
        print("Parando bicicleta.")
        print("Bicicleta parada.")

    def correr(self):
        print("Acelerando...")
        print("Alta velocidade.")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha")
        
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                nro_marcha += 1
                print("Marcha trocada.")
            else:
                print("Não foi possível trocar a marcha")

    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {''.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"