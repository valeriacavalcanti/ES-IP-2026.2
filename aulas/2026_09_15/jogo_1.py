# Jogo para adivinhar 

import random

sorteio = random.randint(1, 100)
print(sorteio)

num = int(input('Número: '))

while num != sorteio and num >= 1 and num <= 100:
    print('Errou!')
    num = int(input('Número: '))


if num == sorteio:
    print('Acertou:', num)
else:
    print('Vai estudar!')
    
    
