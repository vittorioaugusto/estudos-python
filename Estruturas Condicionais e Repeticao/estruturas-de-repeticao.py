texto = input("Informe um texto: ")
vogais = "AEIOU"

# exmeplo utilizando um iterável
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")
else:
    print()


# Exemplo utilizando range
for numero in range(0, 51, 5):
    print(numero, end=" ")

for numero in range(10):
    if numero == 12:
        break
    print(numero, end=" ")

for numero in range(10):
    if numero == 12:
        continue
    print(numero, end=" ")


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    elif numero % 2 == 10:
        continue

    print(numero)
