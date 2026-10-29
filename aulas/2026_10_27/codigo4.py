import random

TAM = 4

# declarar o campo
campo = []
for i in range(TAM):
    campo.append([False] * TAM)

# colocar 6 bombas aleatoriamente
for i in range(6):
    linha = random.randint(0, TAM - 1)
    coluna = random.randint(0, TAM - 1)
    while campo[linha][coluna] == True:
        linha = random.randint(0, TAM - 1)
        coluna = random.randint(0, TAM - 1)
    campo[linha][coluna] = True

print(campo)
    
        
