'''Escreva uma função que receba duas listas e retorne
se elas sao iguais.'''
def iguais(lista1,lista2)->bool:
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            if lista1[i] != lista2[i]:
                return False
        return True
    return False

#Principal
l1 = [1,2,3]
l2 = [1,3]
if (iguais(l1,l2)):   
    print('Iguais')
else:
    print('Diferente')