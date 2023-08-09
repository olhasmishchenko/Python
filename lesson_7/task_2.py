"""Написати калькулятор температури. Користувач
вводить число та тип температури
(C, F, K - Цельсій, Фарренгейт, Кельвін відповідно)
Програма має вивести температуру у трьох шкалах температур –
Цельсій, Фарренгейт, Кельвін."""

user_input_temp = input("Enter the temperature: ")
temperature = float(user_input_temp[:-1])
temperature_scale = str(user_input_temp[-1].upper())
#
if temperature_scale not in ["C", "F", "K"]:
    print("Wrong temperature unit.")
else:
    if temperature_scale == "C":
        fahrenheit = temperature * 9/5 + 32
        kelvin = temperature + 273.15
        print(f"{temperature}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")

    elif temperature_scale == "F":
        celsius = (temperature - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temperature}°F = {celsius:.2f}°C = {kelvin:.2f}K")

    else:
        celsius = temperature - 273.15
        fahrenheit = celsius * 9/5 + 32
        print(f"{temperature}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")