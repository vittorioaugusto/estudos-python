from datetime import datetime, timedelta

data_hora = datetime.today()

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

if tipo_carro == "P":
    data_estimada = data_hora + timedelta(minutes=tempo_pequeno)
    print(f"O Carro chegou: {data_hora} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_hora + timedelta(minutes=tempo_medio)
    print(f"O Carro chegou: {data_hora} e ficará pronto às {data_estimada}")
elif tipo_carro == "G":
    data_estimada = data_hora + timedelta(minutes=tempo_grande)
    print(f"O Carro chegou: {data_hora} e ficará pronto às {data_estimada}")


tempos = {"P": 30, "M": 45, "G": 60}

for tipo_carro, tempo in tempos.items():
    data_estimada = data_hora + timedelta(minutes=tempo)
    print(f"O Carro de tipo '{tipo_carro}' chegou: {data_hora} e ficará pronto às {data_estimada}")


# Exemplo input

tempos = {"P": 30, "M": 45, "G": 60}

tipo_carro = input("Digite 'P' para carro pequeno, 'M' para carro médio, ou 'G' para carro grande: ").upper()

if tipo_carro in tempos:
    tempo = tempos[tipo_carro]
    data_estimada = data_hora + timedelta(minutes=tempo)
    print(f"O Carro de tipo '{tipo_carro}' chegou: {data_hora} e ficará pronto às {data_estimada}")
else:
    print("Tipo de carro inválido. Por favor, digite 'P', 'M', ou 'G'.")




