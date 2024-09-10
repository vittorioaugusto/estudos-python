def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Caio")
exibir_mensagem_3()
exibir_mensagem_3(nome="Marcos")


def calcular_total(numeros):
    return sum(numeros)


print(calcular_total([10, 20, 34]))


def retornar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(retornar_antecessor_sucessor(10))


def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")


salvar_carro(marca="Fiat", modelo="Palio", ano=2001, placa="ABC-1234")
# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 2001, "placa": "ABC-1234"})


def exibir_poema(data_entenso, *args, **kwargs):
    texto = "\n".join(args)
    dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_entenso}\n\n{texto}\n\n{dados}"
    print(mensagem)


exibir_poema(
    "Quarta-feira, 28 de Agosto de 2024",
    "Zen of Python",
    "Beautiful is better thanugly.",
    autor="Tim Peteres",
    ano=1999,
)

