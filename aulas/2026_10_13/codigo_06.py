import random

aposta = [3,7,5,9]

sorteio = random.randint(1,10)

for i in range(len(aposta)):
    if sorteio == aposta[i]:
        break

if aposta[i] == sorteio:
    print('existe', sorteio, i)
else:
    print('nao existe', sorteio, i)

print(aposta)
