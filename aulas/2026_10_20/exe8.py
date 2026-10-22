'''Crie uma função que receba uma lista e retorne
uma cópia da mesma'''
def copia(original:list)->list:
    lista_copia = []

    for i in original:
        lista_copia.append(i)

    return lista_copia

#Programa Principal
nomes = ['Ana','Bia','Ze']
nomes_copia = copia(nomes)

print(nomes_copia)

numeros = [1,2,3,4]
numeros_copia = copia(numeros)
print(numeros_copia)