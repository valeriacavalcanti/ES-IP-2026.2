import random

def validar_numero(valor: int) -> bool:
    if valor >= menor and valor <= maior:
        return True
    else:
        return False


def verificar_acerto(valor: int) -> bool:
    if valor == sorteio:
        return True
    else:
        return False


# Main

#menor, maior = 1, 100
menor, maior = random.randint(0, 10), random.randint(90, 100)

sorteio = random.randint(menor, maior)
#print(sorteio)

num = int(input(f'Número ({menor}-{maior}): '))

while verificar_acerto(num) != True and validar_numero(num) == True:
    if num > sorteio:
        maior = num - 1
        print('Errou: Seu chute foi maior.')
    else:
        menor = num + 1
        print('Errou: Seu chute foi menor.')
    
    #num = int(input(f'Número ({menor}-{maior}): '))
    num = int(input('Número: '))


# saiu do laço
if verificar_acerto(num) == True:
    print('Acertou:', num)
else:
    print('Chute inválido!')
    
    
