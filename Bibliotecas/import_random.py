import statistics
import random

numero_sequencial = list(range(1, 101))
media_sequencial = statistics.mean(numero_sequencial)
variancia_sequencial = statistics.variance(numero_sequencial)

print("Números sequenciais:", numero_sequencial)
print("Média dos números sequenciais:", media_sequencial)
print("Variância dos números sequenciais:", variancia_sequencial)

numero_aleatorio = [random.randint(1, 100) for _ in range(100)]
media_aleatorio = statistics.mean(numero_aleatorio)
variancia_aleatorio = statistics.variance(numero_aleatorio)

print("\nNúmeros aleatórios:", numero_aleatorio)
print("Média dos números aleatórios:", media_aleatorio)
print("Variância dos números aleatórios:", variancia_aleatorio)
