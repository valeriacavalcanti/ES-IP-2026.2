''''
num = 1
qt = 0

while num <= 10:
    if num % 2 == 0:
        print(num)
        qt = qt + 1
    num = num + 1

print(qt, num)
'''

num = 1
qt = 0

while True:
    if num > 10:
        break
    if num % 2 == 0:
        print(num)
        qt = qt + 1
    num = num + 1

print(qt, num)