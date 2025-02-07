def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

fahrenheit = float(input("Temperature in Fahrenheit: "))
print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_centigrade(fahrenheit)} Centigrade.")
