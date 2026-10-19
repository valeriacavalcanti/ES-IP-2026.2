import random

aposta = [0] * 6

for i in range(6):
    while True:
        numero = random.randint(1, 10)

        for j in range(6):
            if numero == aposta[j]:
                break

        if aposta[j] != numero:
            break
            
    aposta[i] = numero

for i in range(6):
    print(i, aposta[i])

print(aposta)
