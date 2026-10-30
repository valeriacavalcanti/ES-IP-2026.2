''''
num = int(input('Número: '))

while num < 0:
    num = int(input('Número: '))

print(num)
'''

while True:
    num = int(input('Número: '))
    if num >= 0:
        break

print(num)