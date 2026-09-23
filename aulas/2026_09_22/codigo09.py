# Ler 10 números e exibir a soma e a média desses números.

soma = 0
QUANTIDADE = 3

for i in range(QUANTIDADE):
    num = int(input(f'Número {i + 1}: '))
    soma = soma + num

media = soma / QUANTIDADE

print('Soma:', soma)
print('Média:', media)
