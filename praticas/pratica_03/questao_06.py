def verificar_validade(dia: int, mes: int, ano: int) -> int:
    from datetime import datetime
    agora = datetime.now()

    if ano > agora.year:
        return 1
    elif ano < agora.year:
        return -1
    elif mes > agora.month:
        return 1
    elif mes < agora.month:
        return -1
    elif dia > agora.day:
        return 1
    elif dia < agora.day:
        return -1
    else:
        return 0


## Main

print("Data de validade do produto:")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

resultado = verificar_validade(dia, mes, ano)

if resultado == 1:
    print('O produto está apto para consumo')
elif resultado == 0:
    print('O produto deve ser consumido hoje')
else:
    print('O produto está vencido')