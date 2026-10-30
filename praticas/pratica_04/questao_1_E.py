''''
num1 = int(input('Número: '))
num2 = int(input('Número: '))

while num1 != 0 and num2 != 0 and num1 != num2:
    print('Eita')
    num1 = int(input('Número: '))
    num2 = int(input('Número: '))

print(num1, num2)
'''

while True:
    num1 = int(input('Número: '))
    num2 = int(input('Número: '))
    if num1 == 0 or num2 == 0 or num1 == num2:
        break
    print('Eita')

print(num1, num2)