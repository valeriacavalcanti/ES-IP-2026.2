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
qtd_acertos = 0

for i in range(6):
    if aposta[i] in sorteio:
        qtd_acertos += 1

if qtd_acertos == 6:
    print('ganhou, está rico')
else:
    print(f'só acertou {qtd_acertos}, continua pobre')
    
