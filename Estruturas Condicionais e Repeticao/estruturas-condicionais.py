maior_idade = 18
menor_idade = 12
idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Você é Adulto")
elif idade >= menor_idade:
    print("Você é Adolescente")
else:
    print("Você é Criança")


saldo = 3000.0
cheque_especial = 500
opcao = int(
    input(
        "Informe uma opção: \n[1] Conta Normal \n[2] Conta Universitária \n[3] Saldo \nOpção: "
    )
)

if opcao == 1:
    saque = float(input("Informe o valor do saque: "))
    if saldo >= saque:
        saldo -= saque
        print(f"Saque de R${saque:.2f} realizado com sucesso!")
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"Cheque Especial disponível: R${cheque_especial:.2f}")
    elif saque <= (saldo + cheque_especial):
        cheque_especial_usado = saque - saldo
        saldo = 0
        cheque_especial -= cheque_especial_usado
        print(f"Saque de R${saque:.2f} realizado com o uso do cheque especial!")
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"Cheque Especial disponível: R${cheque_especial:.2f}")
    else:
        print("Saldo insuficiente para o saque.")
elif opcao == 2:
    saque = float(input("Informe o valor do saque: "))
    if saldo >= saque:
        saldo -= saque
        print(f"Saque de R${saque:.2f} realizado com sucesso!")
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print("Saldo insuficiente para o saque.")
elif opcao == 3:
    print(f"Saldo atual: R${saldo:.2f}")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

print("Obrigado por ser nosso cliente!")
