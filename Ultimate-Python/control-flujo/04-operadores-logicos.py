# And, or, not

bateria = True
gas = True
encendido = True
edad = 18

if gas and encendido:
    print("El auto puede avanzar")

if gas and encendido and edad > 17:
    print("Puedes avanzar")

if gas or bateria:
    print("El auto tiene bateria y gasolina")
else:
    print("El auto no tiene gas o bateria")

if gas and (encendido or edad > 17):
    print("Puedes avanzar")
