mes = int(input('Código do mês = '))

if mes == 2:
    print("28 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 dias")
else:
    print("31 dias")
