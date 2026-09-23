# Ler 4 números e exibir quantos são positivos.

qtd = 0

for i in range(4):
    num = int(input('Número: '))
    if num > 0:
        qtd = qtd + 1

print('quantidade positivo:', qtd)
