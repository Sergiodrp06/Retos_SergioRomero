valorA = float(input("Ingrese la hora de ingreso al aparcamento"))
valorB = float(input("Ingrese la hora de salida del aparcamento"))
hora = valorA-valorB

valorD = int(input("Ingrese el numero 1 si su dia es Lunes, Martes o Miercoles, 2 si su dia es Jueves o Viernes, 3 si su dia es Sabado o Domingo"))

Resultado = int(0)
Resultado1 = int(0)

print("El tiempo en el aparcamento fue de: ")
print(hora)

if valorD == 1:
    Resultado1 = 2*hora
print("El precio a pagar es de: ")
print(Resultado1)

if valorD == 2:
    Resultado1 = 2.5*hora
print("El precio a pagar es de: ")
print(Resultado1)

if valorD == 3:
    Resultado1 = 3*hora
print("El precio a pagar es de: ")
print(Resultado1)