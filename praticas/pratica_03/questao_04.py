def obter_maior(valor1, valor2):
    if valor1 >= valor2:
        return valor1
    else:
        return valor2


## Main

# Primeira pessoa
idade1 = int(input('Idade: '))
altura1 = float(input('Altura: '))
peso1 = float(input('Peso: '))
salario1 = float(input('Salário: '))

# Segunda pessoa
idade2 = int(input('Idade: '))
altura2 = float(input('Altura: '))
peso2 = float(input('Peso: '))
salario2 = float(input('Salário: '))


maior_idade = obter_maior(idade1, idade2)
print('Maior idade:', maior_idade)

maior_altura = obter_maior(altura1, altura2)
print('Maior altura:', maior_altura)

maior_peso = obter_maior(peso1, peso2)
print('Maior peso:', maior_peso)

maior_salario = obter_maior(salario1, salario2)
print('Maior salário:', maior_salario)