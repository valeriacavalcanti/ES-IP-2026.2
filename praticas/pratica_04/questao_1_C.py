''''
num = int(input('Número: '))

while (num < 0) or (num > 100):
    num = int(input('Número: '))

print(num)
'''

while True:
    num = int(input('Número: '))
    if num >= 0 and num <= 100:
        break

print(num)