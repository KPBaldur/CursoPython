texto = "Hola Mundo"
print(texto)

#Pasara todo en mayusculas
print("upper")
print(texto.upper())

#Pasara todo en minusculas
print("lower")
print(texto.lower())

#Convierte el primer caracter de la cadena en mayuscula
print("capitalize")
print(texto.capitalize())

#Convierte el primer caracter de la cadena en minuscula(mas agresivo que lower)
print("casefold")
print(texto.casefold())

#Intercambia mayusculas y minusculas en la cadena
print("swapcase")
print(texto.swapcase())

#Convierte el primer caracter de cada palabra en mayuscula
print("title")
print(texto.title())

print(texto.find("Mun"))
nuevoTexto = texto.replace("Mun", "Man")
print(nuevoTexto)
print("Mundo" in texto)