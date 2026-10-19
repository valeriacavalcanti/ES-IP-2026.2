nomes = [''] * 4
idades = [0]* 4

for i in range(4):
    nomes[i] = input('Nome: ')
    idades[i] = int(input('Idade: '))

for i in range(4):
    print(f'{nomes[i]} {idades[i]}')

