n1 = int(input("Primeiro número: "))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)