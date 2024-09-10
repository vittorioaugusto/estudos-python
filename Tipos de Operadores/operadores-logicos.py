print(True and True)
print(True and False)
print(True or True)
print(True or False)

print("\nExemplos: ")

idade = 20
curso_basico_completado = True
pode_inscrever = (idade >= 18) and curso_basico_completado
print(pode_inscrever)


numero = 9
if (numero % 3 == 0) or (numero % 5 == 0):
    print(f"O número {numero} é divisível por 3 ou 5.")
else:
    print(f"O número {numero} não é divisível nem por 3 nem por 5.")


senha = ""
if not senha:
    print("A senha não pode estar vazia.")
else:
    print("Senha aceita.")
