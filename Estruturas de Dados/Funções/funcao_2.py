def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def exibir_resultado(a, b, funcao, operador):
    resultado = funcao(a, b)
    print(f"O resultado de {a} {operador} {b} = {resultado}")


exibir_resultado(10, 10, somar, "+")
exibir_resultado(10, 10, subtrair, "-")
exibir_resultado(10, 10, multiplicar, "*")
exibir_resultado(10, 10, dividir, "/")



# Exemplo input 

def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 == 0:
        return "Erro: Divisão por zero"
    return numero1 / numero2


def media(numero1, numero2):
    return (numero1 + numero2) / 2


def exibir_resultado(numero1, numero2, funcao, operacao):
    resultado = funcao(numero1, numero2)
    if operacao == "média entre":
        print(f"A média entre {numero1} e {numero2} = {resultado}")
    else:
        print(f"O resultado de {numero1} {operacao} {numero2} = {resultado}")


print("Escolha a operação desejada:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Média entre")

opcao = input("Digite o número da operação: ")

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

if opcao == "1":
    exibir_resultado(numero1, numero2, somar, "+")
elif opcao == "2":
    exibir_resultado(numero1, numero2, subtrair, "-")
elif opcao == "3":
    exibir_resultado(numero1, numero2, multiplicar, "*")
elif opcao == "4":
    exibir_resultado(numero1, numero2, dividir, "/")
elif opcao == "5":
    exibir_resultado(numero1, numero2, media, "média entre")
else:
    print("Opção inválida. Por favor, escolha um número de 1 a 5.")
