# Ler um número inteiro. Calcular e exibir o fatorial desse número.

fatorial = 1
num = int(input('Número: '))

for i in range(1, num + 1):
    fatorial = fatorial * i

print(f'{num}! = {fatorial}')
