TAMANHO = 10

nomes = ['']*TAMANHO

for i in range(TAMANHO):
    nomes[i]=input('Nome: ')

j = TAMANHO-1

for i in range(TAMANHO//2):
    nomes[i],nomes[j]=nomes[j],nomes[i]
    j-=1

print(nomes)