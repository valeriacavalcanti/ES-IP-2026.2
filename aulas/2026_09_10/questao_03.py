def calcula_juros(valor: float) -> float:
    return valor * 0.04

def calcula_multa(valor: float) -> float:
    return valor * 0.1


def valor_total_a_pagar(valor: float) -> float:
    juros = calcula_juros(valor)
    multa = calcula_multa(valor)
    return valor + juros + multa

# Main

valor_divida = float(input('Valor da dívida: '))
total = valor_total_a_pagar(valor_divida)

print(f'Valor total da dívida: R$ {total:.2f}')
