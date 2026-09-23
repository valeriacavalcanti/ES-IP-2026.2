# Ler 10 números e exibir a soma e a média desses números.

soma = 0

for i in range(4):
    num = int(input(f'Número {i + 1}: '))
    soma = soma + num

media = soma / (i + 1)

print('Soma:', soma)
print('Média:', media)
