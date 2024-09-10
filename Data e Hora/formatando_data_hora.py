from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

data_ptbr = "%d/%m/%Y"
hora_ptbr = "%H:%M"
dia_ptbr = "%A"

data_hora_atual = datetime.now()

print(data_hora_atual.strftime(data_ptbr))
print(data_hora_atual.strftime(hora_ptbr))
print(data_hora_atual.strftime(dia_ptbr))
print(
    f"Horário: {data_hora_atual.strftime(hora_ptbr)} \nData: {data_hora_atual.strftime(data_ptbr)} \nDia da Semana: {data_hora_atual.strftime(dia_ptbr).title()}"
)
