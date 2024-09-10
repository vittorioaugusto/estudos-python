def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print(f"Valor sacado R${valor}")
    else:
        print(f"Valor para saque insuficiente")

    print("Obrigado por ser nosso cliente")


sacar(500)

valor_saque = float(input("Digite o valor que deseja sacar: "))
sacar(valor_saque)