soma = 0

for i in range(3):
    num = int(input(f'{i + 1}° Número: '))
    soma = soma + num

media = soma / (i + 1)

if num > media:
    print(num, 'acima da média')
else:
    print(num, 'não acima da média')

print(soma)
print(media)
