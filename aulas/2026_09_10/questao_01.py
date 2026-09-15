valor_mensalidade = float(input('Mensalidade: '))

valor_matricula = valor_mensalidade * 0.2
desconto = valor_mensalidade * 0.12
valor_anual = valor_mensalidade - desconto

print(f'Anual: {valor_matricula} + 12 x {valor_anual}')
print(f'Mensal: {valor_matricula} + 12 x {valor_mensalidade}')
