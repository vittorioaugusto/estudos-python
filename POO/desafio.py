class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def andar(self):
        print("Bicicleta se movimentando")

    def correr(self):
        print("Vrummmmm")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bicicleta_1 = Bicicleta("Vermelha", "Oggi", 2021, 1200)
print(bicicleta_1.cor, bicicleta_1.modelo, bicicleta_1.ano, bicicleta_1.valor)

bicicleta_2 = Bicicleta("Azul", "Scott", 2024, 5000)
print(bicicleta_2.cor, bicicleta_2.modelo, bicicleta_2.ano, bicicleta_2.valor)

bicicleta_3 = Bicicleta("Preto", "Caloi", 2022, 1000)
print(bicicleta_3)

bicicleta_1.andar()
bicicleta_1.correr()

bicicleta_2.andar()
bicicleta_2.parar()
