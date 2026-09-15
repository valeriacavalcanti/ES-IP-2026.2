def calcular_frete(distancia: float, peso: float) -> float:
    if distancia > 100:
        frete = -1
    else:
        if peso < 5:
            frete = 10 + (0.5 * distancia)
        else:
            if peso <= 20:
                frete = 20 + (0.8 * distancia)
            else:
                frete = 40 + (1.2 * distancia)

    return frete

# main

peso = float(input('Peso: '))
distancia = float(input('Distância: '))

frete = calcular_frete(distancia, peso)

if frete != -1:
    print(f'Valor do frete: R$ {frete:.2f}')
else:
    print('Região não atendida')
    
