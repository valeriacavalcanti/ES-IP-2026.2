
def media_aritmetica(valor1: int, valor2: int, valor3: int) -> int:
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


def media_ponderada(valor1: int, valor2: int, valor3: int) -> int:
    soma = valor1 * 5 + valor2 * 3 + valor3 * 2
    media = soma / 10
    return media


def calcular_media(valor1: int, valor2: int, valor3: int) -> int:
    ma = media_aritmetica(valor1, valor2, valor3)
    mp = media_ponderada(valor1, valor2, valor3)
    
    if ma > mp:
        return ma
    else:
        return mp


def verificar_aprovado(valor1: int, valor2: int, valor3: int) -> bool:
    media = calcular_media(valor1, valor2, valor3)
    if (media >= 70):
        return True
    else:
        return False


## Programa Principal

nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
nota3 = int(input('Terceira nota: '))

ma = media_aritmetica(nota1, nota2, nota3)
mp = media_ponderada(nota1, nota2, nota3)
maior_m = calcular_media(nota1, nota2, nota3)
situacao = verificar_aprovado(nota1, nota2, nota3)

print(f"Média aritmética: {ma}")
print(f"Média Ponderada: {mp}")
print(f"Maior Média: {maior_m}")

if situacao == True:
    print("Situação acadêmica: Aprovado")
else:
    print("Situação acadêmica: Reprovado")