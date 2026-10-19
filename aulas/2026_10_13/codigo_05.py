import random

aposta = [3,7,5,9]

sorteio = random.randint(1,10)

existe = False
for i in range(len(aposta)):
    if sorteio == aposta[i]:
        existe = True
        break

if existe == True:
    print('existe', sorteio)
else:
    print('nao existe', sorteio)

print(aposta)
