# Ler 10 números e exibir a soma desses números.

soma = 0

for i in range(10):
    num = int(input(f'Número {i + 1}: '))
    soma = soma + num

print('Soma:', soma)
