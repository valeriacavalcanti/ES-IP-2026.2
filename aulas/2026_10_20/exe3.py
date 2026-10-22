'''Leia o nome e idade de 20 estudantes. Ao final,
informe a idade e o nome do estudante mais velho'''

TAMANHO = 20

nomes = ['']*TAMANHO
idades = [0]*TAMANHO

for i in range(TAMANHO):
    nomes[i] = input(f'Qual o nome do {i+1}° aluno? ')
    idades[i] = int(input(f'Qual a idade do {i+1}° aluno? '))

#Encontrando o mais velho
velho = 0

for i in range(1,TAMANHO):
    if idades[i]>idades[velho]:
        velho=i

#Mais velho
print(nomes[(velho)])
print(idades[velho])