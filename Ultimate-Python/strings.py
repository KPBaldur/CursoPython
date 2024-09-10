#relacion basica
nombre_curso = "Ultimate Python"
descripcion_curso = """
Este curso contempla todos los detalles
que se pueden utilizar para encontrar 
un trabajo como programador.
"""

#Saber el largo de una variable
print(len(nombre_curso))

#Obtener un caracter de la variable
print(nombre_curso[0])

#Traer el numero de caracteres de nuestra variable 
#1 desde que caracter
#2 hasta que caracter
#                  1 2
#                 ⬇️⬇️
print(nombre_curso[0:8])

#Traer desde un caracter hasta el final
print(nombre_curso[9:])

#Traer desde el inicio hasta un punto
print(nombre_curso[0:8])

#Traer todo el contenido del string
print(nombre_curso[:])