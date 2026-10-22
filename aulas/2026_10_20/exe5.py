'''Escreva um programa para ler 10 nomes.
Em seguida, imprima os nomes em ordem de leitura 
e em ordem inversa , alterando o conteudo da lista'''

nomes = [''] * 5

for i in range(len(nomes)):
    nomes[i] = input('Nome: ')

n, m = 0, len(nomes) - 1

print(nomes)

while True:
    if n == m or n == m + 1:
        break
    nomes[n], nomes[m] = nomes[m], nomes[n]

    n += 1
    m -= 1

print(nomes)