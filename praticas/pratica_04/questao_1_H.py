''''
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

while a < b:
    print(f"a = {a}, b = {b}")
    a += 1
    b -= 1

print("Loop encerrado.")
'''

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

while True:
    if a >= b:
        break
    print(f"a = {a}, b = {b}")
    a += 1
    b -= 1

print("Loop encerrado.")