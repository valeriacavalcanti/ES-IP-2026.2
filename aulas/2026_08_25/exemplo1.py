"""
IFPB - Campus João Pessoa
Engenharia de Software
Introdução a Programacao

Objetivo:
Obter nome e idade de uma pessoa. Ao final, exibir se ela pode votar.
"""

nome = input('Informe seu nome: ')

idade = input('Informe sua idade: ')
idade = int(idade)

# idade = int(input('Informe sua idade: '))

# analise = idade >= 16

if (idade >= 16):
    print('Parabéns')
    print('Pode votar')
    print('eita')
else:
    print('Que pena')
    print('Você naaaaao pode votar')
    print('He he')

print(f'{nome} você tem {idade} anos.')
#print(f'Pode votar: {analise}')

