import random

def criar_matriz(linhas: int, colunas: int) -> list:
    m = []
    for i in range(TAM):
        m.append([0] * TAM)
    return m

def inserir_bombas(matriz: list, qtd: int):
    for i in range(qtd):
        linha = random.randint(0, TAM - 1)
        coluna = random.randint(0, TAM - 1)
        while matriz[linha][coluna] == -1:
            linha = random.randint(0, TAM - 1)
            coluna = random.randint(0, TAM - 1)
        matriz[linha][coluna] = -1

# main

TAM = 4

# declarar o campo
campo = criar_matriz(TAM, TAM)

# colocar 6 bombas aleatoriamente
inserir_bombas(campo, 4)

print(campo)
    
        
