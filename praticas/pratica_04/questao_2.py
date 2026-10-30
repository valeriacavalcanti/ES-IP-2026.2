qtd_igual = 0

num1 = int(input('Número 01: '))
num2 = int(input('Número 02: '))

while num1 > 0 and num2 > 0:
    if num1 == num2:
        qtd_igual = qtd_igual + 1

    num1 = int(input('Número 01: '))
    num2 = int(input('Número 02: '))

print(qtd_igual)