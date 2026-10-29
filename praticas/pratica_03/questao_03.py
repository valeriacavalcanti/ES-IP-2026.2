def calcular_valor_usd(valor_unitario_usd: float, quantidade: int) -> float:
    return valor_unitario_usd * quantidade


def converter_usd_para_brl(valor_usd: float) -> float:
    cotacao = 5.00
    return valor_usd * cotacao


def calcular_imposto_brl(valor_compra_brl: float) -> float:
    if valor_compra_brl <= converter_usd_para_brl(50.00):
        imposto = valor_compra_brl * 0.20
    else:
        imposto = valor_compra_brl * 0.60
    return imposto


def calcular_valor_final_brl(valor_compra_brl: float) -> float:
    imposto = calcular_imposto_brl(valor_compra_brl)
    return valor_compra_brl + imposto_brl


## Main

valor_unitario = float(input("Digite o valor unitário do produto (USD): "))
quantidade = int(input("Digite a quantidade comprada: "))

valor_usd = calcular_valor_usd(valor_unitario, quantidade)
valor_brl = converter_usd_para_brl(valor_usd)
imposto_brl = calcular_imposto_brl(valor_brl, valor_usd)
valor_final_brl = calcular_valor_final_brl(valor_brl, imposto_brl)

print(f"Valor da compra em USD: US$ {valor_usd:.2f}")
print(f"Valor da compra em BRL (sem taxa): R$ {valor_brl:.2f}")
print(f"Valor da taxa de importação em BRL: R$ {imposto_brl:.2f}")
print(f"Valor final da compra em BRL: R$ {valor_final_brl:.2f}")