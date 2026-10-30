while True:
    numero = int(input("Digite um número positivo (ou 0 para sair): "))
    if numero == 0:
        break
    print(f"Você digitou: {numero}")
    if numero < 0:
        print("Número negativo não é permitido.")

print("Encerrando o loop.")