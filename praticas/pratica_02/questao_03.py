nome1 = input('Nome: ')
idade1 = int(input('Idade: '))

nome2 = input('Nome: ')
idade2 = int(input('Idade: '))

if idade1 > idade2:
    print(nome1)
elif idade2 > idade1:
    print(nome2)
else:
    print("Empate")