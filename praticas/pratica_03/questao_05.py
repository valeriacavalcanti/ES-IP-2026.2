def comparar_numeros(num1: int, num2: int) -> int:
    if num1 > num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1


## Main (testar a função)

print(f"{comparar_numeros(10, 20) = }")
print(f"{comparar_numeros(10, 10) = }")
print(f"{comparar_numeros(20, 10) = }")
