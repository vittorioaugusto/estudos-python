saldo = 500
saque = 1000

print(saldo >= saque)
print(saldo <= saque)
print(saldo != saque)
print(saldo == saque)

print("\nExemplo")

saldo = 1000.00
valor_saque = float(input("Digite o valor que deseja sacar: R$ "))

if valor_saque > saldo:
    print("Saldo insuficiente!")
else:
    saldo -= valor_saque
    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    print(f"Saldo atual: R$ {saldo:.2f}")
