# declarar a matriz

matriz = [[10,20,30], [40,50,60], [70,80,90], [100,110,120]]
LINHAS = 4
COLUNAS = 3


# exibir TODOS os elementos da matriz

for i in range(LINHAS):
    for j in range(COLUNAS):
        print(i, j, matriz[i][j])


# exibir a soma dos elementos POR LINHA

for i in range(LINHAS):
    soma = 0
    for j in range(COLUNAS):
        soma += matriz[i][j]
    print(i, soma)


print('colunas')
# exibir a soma dos elementos POR COLUNA
for j in range(COLUNAS):
    soma = 0
    for i in range(LINHAS):
        soma += matriz[i][j]
        #print(i, j)
    print(j, soma)
