import random

aposta = [0] * 6
sorteio = []

# ler a aposta do usuário
for i in range(6):
    aposta[i] = int(input(f'Número {i + 1}: '))

# gerar o sorteio
while len(sorteio) < 6:
    numero = random.randint(1, 10)
    if numero not in sorteio:
        sorteio.append(numero)

# verificar quantos números acertou
acertos = []

for i in range(6):
    if aposta[i] in sorteio:
        acertos.append(aposta[i])

if len(acertos) == 6:
    print('ganhou, está rico')
else:
    print(f'só acertou {acertos}, continua pobre')
    
