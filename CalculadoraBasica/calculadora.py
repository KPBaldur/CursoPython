print("Bienvenido a la calculadora")
print("Ingrese la operacion")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
operacion= int(input("Operacion: "))

n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))

if operacion == 1:
    suma = n1 + n2
    print("El resultado de la suma es: ", suma)
elif operacion == 2:
    resta = n1 - n2
    print("El resultado de la suma es: ", resta)
elif operacion == 3:
    multi = n1 * n2
    print("El resultado de la suma es: ", multi)
elif operacion == 4:
    if n2 != 0:
        div = n1 / n2
        print("El resultado de la suma es: ", div)
    else:
        print("Error: no se puede dividir por cero.")
else:
    print("Parametros incorrectos")