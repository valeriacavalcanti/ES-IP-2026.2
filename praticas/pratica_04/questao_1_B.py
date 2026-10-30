''''
num = int(input('Número: '))
qt = 0

while num >= 0:
    if num == 0:
        qt = qt + 1
    num = int(input('Número: '))

print(qt, num)
'''

qt = 0

while True:
    num = int(input('Número: '))
    if num < 0:
        break
    if num == 0:
        qt = qt + 1

print(qt, num)