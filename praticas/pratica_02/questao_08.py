a = int(input('Lado 1: '))
b = int(input('Lado 2: '))
c = int(input('Lado 3: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b and b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não forma um triângulo")