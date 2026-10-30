''''
num1 = int(input('Número: '))
num2 = int(input('Número: '))

while num1 > 0 and num2 > 0:
    print('Eita')
    if num1 == num2:
        break
    num1 = int(input('Número: '))
    num2 = int(input('Número: '))

print(num1, num2)
'''

num1 = int(input('Número: '))
num2 = int(input('Número: '))

while True:
    if num1 <= 0 or num2 <= 0:
        break
    print('Eita')
    if num1 == num2:
        break
    num1 = int(input('Número: '))
    num2 = int(input('Número: '))

print(num1, num2)