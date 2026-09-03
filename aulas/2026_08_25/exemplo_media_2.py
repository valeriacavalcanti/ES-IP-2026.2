nome = input('Informe seu nome: ')

media = input('Informe sua média: ')
media = int(media)

if (media >= 70):
    print('Aprovado')
    
if (media < 40):
   print('Reprovado')

if ((media >= 40) and (media < 70)):
    print('Final')
