''''
qtd = 0

while True:

    nome = input('Nome: ')
    if nome == 'FIM' or nome == 'fim':
        break

    qtd = qtd + 1

print(qtd)
'''

qtd = 0

nome = input('Nome: ')
while nome != 'FIM' and nome != 'fim':
    qtd = qtd + 1
    nome = input('Nome: ')

print(qtd)