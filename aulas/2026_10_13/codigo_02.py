soma = 0

# declarar vetor de tamanho 3
numeros = [0,0,0]

# percorrer o vetor para armazenar
for i in range(3):
    numeros[i] = int(input(f'{i + 1}° Número: '))
    soma = soma + numeros[i]

media = soma / (i + 1)

# percorrer o vetor para ler
for i in range(3):
    if numeros[i] > media:
        print(numeros[i], 'acima da média')
    else:
        print(numeros[i], 'não acima da média')

print(soma)
print(media)
