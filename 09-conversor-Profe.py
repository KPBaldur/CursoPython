temperatura = float(input("Ingrese temperatura:"))
escala = input("Es Fahrenheit(F) o es Celcius(C):").lower()

if escala == "f":
    celcius = (temperatura - 32) * 5/9
    print(celcius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print(fahrenheit)