'''Leia 10 valores inteiros e os armazenem em uma lista. Ao final
informe qual o maior valor da lista'''
numeros = [0]*10

for i in range(len(numeros)):
    numeros[i] = int(input(f'{i+1}° valor: '))

#Procurando o maior valor
maior = numeros[0]

for i in range(1,len(numeros)):
    if numeros[i]>maior:
        maior=numeros[i]

print(f'Maior valor: {maior}')