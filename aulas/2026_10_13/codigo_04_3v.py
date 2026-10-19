import random

aposta = []

while len(aposta) < 6:
    numero = random.randint(1, 10)
    if numero not in aposta:
        #aposta = aposta + [numero]
        aposta.append(numero)


for i in range(6):
    print(i, aposta[i])

print(aposta)
