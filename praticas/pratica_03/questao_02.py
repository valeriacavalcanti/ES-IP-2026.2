def celsius_para_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def celsius_para_kelvin(celsius: float) -> float:
    kelvin = celsius + 273.15
    return kelvin


## Main

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius_para_fahrenheit(celsius)
kelvin = celsius_para_kelvin(celsius)

print(f"Temperatura em Fahrenheit: {fahrenheit}")
print(f"Temperatura em Kelvin: {kelvin}")