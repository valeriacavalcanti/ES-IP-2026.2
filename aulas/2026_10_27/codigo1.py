# declarar a matriz

matriz = []
for i in range(6):
    matriz.append([0] * 3)

# exibir tudo
print(matriz)

# exibir por linha
for i in range(6):
    print(i, matriz[i])


# exibir por elemento (todas as linhas)
for i in range(6):
    for j in range(3):
        print(i, j, matriz[i][j])

