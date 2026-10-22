'''Função que retorna o maior elemento de uma lista'''
def max(numeros):
    #Procurando o maior valor
    maior = numeros[0]

    for i in range(1,len(numeros)):
        if numeros[i]>maior:
            maior=numeros[i]

    return maior

def min(numeros):
    #Procurando o maior valor
    menor = numeros[0]

    for i in range(1,len(numeros)):
        if numeros[i]<menor:
            menor=numeros[i]

    return menor

'''Leia 10 valores inteiros e os armazenem em uma lista. Ao final
informe qual o maior valor da lista'''
numeros = [0]*5

'''for i in range(len(numeros)):
    numeros[i] = int(input(f'{i+1}° valor: '))'''

print(f'Maior valor: {max(numeros)}')

valores = [1,2,3,4,5,6,7,-1]
print(f'Maior valor: {max(valores)}')
print(f'Menor valor: {min(valores)}')