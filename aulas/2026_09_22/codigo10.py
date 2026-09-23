# Ler um número inteiro. Calcular e exibir a soma dos números de 1 até
# o número digitado.

soma = 0
num = int(input('Número: '))

for i in range(1, num + 1):
    soma = soma + i

print(soma)
