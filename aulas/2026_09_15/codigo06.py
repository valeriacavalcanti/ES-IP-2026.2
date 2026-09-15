# Ler 3 números e ao final exibir a soma dos números digitados
# Codigo04 adaptado para usar while True.

qtd = 0
soma = 0

while True:
    num = int(input('Número: '))
    soma = soma + num
    qtd = qtd + 1

    if qtd == 3:
        break

print(f'Foram digitados {qtd} numeros e o último foi {num} e soma é {soma}')
