menu = """
Bienvenido al convertidor universal!
Ingrese el convertidor que desea ingresar:
1. Convertidor Distancia
2. Convertidor Temperatura
3. Convertidor Peso 
4. Salir"""

print(menu)

while True:
    try:
        opcion = int(input("Ingrese su opcion: "))
    except ValueError:
        print("Error: Porfavor ingrese un numero valido para la opcion")
        continue

    if opcion == 4:
        print("Saliendo del programa, hasta pronto......")
        break

    if opcion == 1:
        print("Convertidor de 'Distancia' seleccionado:")
        try:
            distancia = float(input("Ingrese la distancia: "))
        except ValueError:
            print("Error: Porfavor ingrese un numero valido para la distancia")
            continue
        
        opDistancia = input("Desea convertir a Kilometros(K) O Millas(M): ")
        if opDistancia.lower() == "k":
            resultado = distancia * 1.60934
            print ("La nueva distancia de Kilometros es de: ", resultado)
        elif opDistancia.lower() == "m":
            resultado = distancia * 0.621371
            print ("La nueva distancia de millas es de: ",resultado)
        else:
            print("Ingrese una opcion valida")

    elif opcion == 2:
        print("Convertidor de 'Temperatura' seleccionado")
        try:
            temperatura = float(input("Ingrese la temperatura: "))
        except ValueError:
            print("Error: Porfavor ingrese un numero valido para la temperatura")
        
        opTemperatura = input("Desea convertir a Fahrenheit(F) o Celcius(C): ")
        if opTemperatura.lower() == 'f':
            resultado = (temperatura * 1.8) + 32
            print ("La nueva temperatura en Fahrenheit es de: ", resultado)
        elif opTemperatura.lower() == 'c':
            resultado = (temperatura - 32) * 5/9
            print("La nueva tempera en Celcius es de: ", resultado)
        else:
            print("Ingrese una opcion valida")

    elif opcion == 3:
        print("Convertidor de 'Peso' seleccionado")
        try:
            peso = float(input("Ingrese el Peso: "))
        except ValueError:
            print("Error: Porfavor ingrese un numero valido para el peso")

        opPeso = input("Desea convertir en Kilogramo(k) o Libra(l): ")
        if opPeso.lower() == "l":
            resultado = peso * 2.205 
            print("El nuevo peso en Libras es de: ", resultado)
        elif opPeso.lower() == "k":
            resultado = peso * 0.45359237
            print("El nuevo peso en Kilogramos es de: ", resultado)
        else:
            print("Ingresa una opcion valida")
    else:
        print("Ingresa una opcion valida")
