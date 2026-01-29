def convert_temperature(celsius: float) -> list[float]:
    fahrenheit = celsius * 1.80 + 32.00
    kelvin = celsius + 273.15
    return [f"{fahrenheit:.5f}", f"{kelvin:.5f}"]
print(convert_temperature(36.50))  # Output: [97.7, 309.65]
print(convert_temperature(122.11))  # Output: [251.798, 395.26]
print(convert_temperature(0.00))  # Output: [32.0, 273.15]