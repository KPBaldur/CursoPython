temp = input("Ingrese la temperatura a convertir: ")
tempNum = float(temp)
opcion = input("En Fahrenheit(F) o Celcius(C)?: ")

if opcion.lower() == 'c':
    
    resultado = (tempNum - 32) * 5/9
    #resultado * 0,555
    print(resultado)
elif opcion.lower() == 'f':
    print("Elegiste Fahrenheit")
    resultado = tempNum * 1.8 + 32
    print(resultado)
else:
    print("Ingrese una opcion valida")