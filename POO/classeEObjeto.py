class Usuario:
    def __init__(self, nome, idade, acordado=True):
        self.nome = nome
        self.idade = idade
        self.acordado = acordado

    def falar(self):
        print("Olá pessoal")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


pessoa_1 = Usuario("José", 25)
print(pessoa_1.nome, pessoa_1.idade, pessoa_1.acordado)

pessoa_2 = Usuario("João", 58, False)
print(pessoa_2.nome, pessoa_2.idade, pessoa_2.acordado)

pessoa_3 = Usuario("Maria", 42)
print(pessoa_3)

pessoa_1.falar()
pessoa_1.dormir()

pessoa_2.falar()
pessoa_2.dormir()
