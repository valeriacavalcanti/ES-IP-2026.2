temperatura = float(input('Informe a temperatura: '))

if temperatura < 10:
    print("Muito Frio")
elif temperatura <= 15:
    print("Frio")
elif temperatura <= 25:
    print("Agradável")
elif temperatura <= 30:
    print("Quente")
else:
    print("Muito Quente")