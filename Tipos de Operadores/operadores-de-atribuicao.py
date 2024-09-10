valor = 50
valor += 20
print(valor)

valor = 20
valor -= 10
print(valor)

valor = 30
valor //= 10
print(valor)

print("\nExemplo")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

numero1 += numero2
print(f"Após adicionar {numero2} ao primeiro número: {numero1}")

numero1 -= numero2
print(f"Após subtrair {numero2} do primeiro número: {numero1}")

numero1 *= numero2
print(f"Após multiplicar o primeiro número por {numero2}: {numero1}")

if numero2 != 0:
    numero1 /= numero2
    print(f"Após dividir o primeiro número por {numero2}: {numero1}")
else:
    print("Divisão por zero não é permitida.")
