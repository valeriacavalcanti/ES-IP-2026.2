import random

def validar_numero(valor: int) -> bool:
    if valor >= 1 and valor <= 100:
        return True
    else:
        return False


def verificar_acerto(valor: int) -> bool:
    if valor == sorteio:
        return True
    else:
        return False


# Main

sorteio = random.randint(1, 100)
#print(sorteio)

num = int(input('Número: '))

while verificar_acerto(num) != True and validar_numero(num) == True:
    if num > sorteio:
        print('Errou: Seu chute foi maior.')
    else:
        print('Errou: Seu chute foi menor.')
    
    num = int(input('Número: '))


# saiu do laço
if verificar_acerto(num) == True:
    print('Acertou:', num)
else:
    print('Vai estudar!')
    
    
