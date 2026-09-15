def area_retangulo(base: float, altura: float) -> float:
    return base * altura

def perimetro_retangulo(base: float, altura: float) -> float:
    return 2 * (base + altura)

def valor_terreno(area: float, preco_m2: float) -> float:
    return area * preco_m2


# Main

largura = float(input('Largura: '))
altura = float(input('Altura: '))
valor_metro_2 = float(input('Metro Quadrado: '))

area = area_retangulo(largura, altura)
perimetro = perimetro_retangulo(largura, altura)
valor = valor_terreno(area, valor_metro_2)

print(f'Área do Terreno: {area}')
print(f'Perímetro do Terreno: {perimetro}')
print(f'Valor do Terreno: R$ {valor:.2f}')
