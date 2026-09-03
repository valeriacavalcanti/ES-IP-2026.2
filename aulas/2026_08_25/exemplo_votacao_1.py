nome = input('Informe seu nome: ')

media = input('Informe sua média: ')
media = int(media)

if (media >= 70):
    print('Aprovado')
else:
    if (media >= 40):
        print('Final')
    else:
        print('Reprovado')
