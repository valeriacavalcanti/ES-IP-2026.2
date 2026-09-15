# Ler e validar um número positivo.

num = int(input('Número: '))

while num <= 0:
    print('Número inválido')
    num = int(input('Número: '))

print('Número positivo:', num)