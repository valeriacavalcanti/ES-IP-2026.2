# Ler 3 números e ao final exibir a soma dos números digitados

qtd = 0
soma = 0

while qtd < 3:
    num = int(input('Número: '))
    soma = soma + num
    qtd = qtd + 1

print(f'Foram digitados {qtd} numeros e o último foi {num} e soma é {soma}')