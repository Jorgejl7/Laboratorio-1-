#Ejericio 9: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad = float(input("Ingrese el la cantidad a invertir: Q"))
interes = float(input("Interes anual: %"))
años = float(input("tiempo en años: "))
capital= round(cantidad*(interes/100+1)** años,2)
print(" el capital obtenido es de: Q",capital)
