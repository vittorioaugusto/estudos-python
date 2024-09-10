nome = "vItToRio"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Como foi o seu dia?  "

print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print(menu.center(15, "#"))
print(".".join(menu))


nome_2 = "Carlos"

mensagem = f"""
    ##### MENU #####
    
    Olá meu nome é {nome_2}
        Essa mensagem tem diferentes
    Nível: 1
"""

print(mensagem)
