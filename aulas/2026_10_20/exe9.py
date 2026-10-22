'''Função que retorna a união de duas listas'''
def uniao(lista1,lista2):
    lista_unida = []

    for elemento in lista1:
        lista_unida.append(elemento)

    for elemento in lista2:
            lista_unida.append(elemento)

    return lista_unida

#Programa Principal
l1 = [1,2,3]
l2 = [4,5,6,7]

lista_u = uniao(l1,l2)
print(lista_u)