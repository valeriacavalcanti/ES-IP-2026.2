VALOR_CUPOM = 50

valor = float(input('Valor da compra: '))

if (valor <= 100):
    desconto = valor * 0.1
    valor = valor - desconto

    # valor -= desconto
    # valor = valor * 0.9
    
    # 90% do valor
    #valor *= 0.9

    print(f'Valor com desconto de 10%: R$ {valor:.2f}')
else:
    if (valor <= 200):
        valor_parcela = valor / 4
        print(f'4 parcelas de R$ {valor_parcela:.2f}')
    else:
        if (valor <= 400):
            valor = valor * 0.7
            print(f'Valor com desconto de 30%: R$ {valor:.2f}')
        else:
            qtd_cupons = int(valor // VALOR_CUPOM)
            saldo = valor % VALOR_CUPOM
            falta_novo_cupons = VALOR_CUPOM - saldo
            
            print(f'R$ {valor:.2f} = {qtd_cupons} cupons.')
            print(f'Compre mais R$ {falta_novo_cupons:.2f} e receba mais um cupom.')
            
            
