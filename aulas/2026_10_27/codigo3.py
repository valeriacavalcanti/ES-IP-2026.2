'''
Uma escola tem 4 turmas, em cada turma tem 20 alunos.

Escreva um programa para ler as notas de todos os alunos, em todas
as Turmas.

'''

import random

TURMAS = 2 # 4
ALUNOS = 4 # 20

# declarar a matriz
matriz = []
for i in range(TURMAS):
    matriz.append([0] * ALUNOS)

# preencher a matriz com notas aleatórias entre 0 e 100
for i in range(TURMAS):
    for j in range(ALUNOS):
        matriz[i][j] = random.randint(0, 100)

# exibir as notas por TURMA
for i in range(TURMAS):
    print(matriz[i])


# exibir a média de cada TURMA
for i in range(TURMAS):
    soma = 0
    for j in range(ALUNOS):
        soma += matriz[i][j]
    media_turma = soma / ALUNOS
    print(i, media_turma)

# exibir a média de cada posição em cada turma
for j in range(ALUNOS):
    soma = 0
    for i in range(TURMAS):
        soma += matriz[i][j]
    media_posicao = soma/TURMAS
    print(j, media_posicao)
