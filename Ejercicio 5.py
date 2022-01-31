#Ejercicio 5: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas_trabajadas = float (input("Ingrese el total de horas trabajas por el empleado: "))
costo_horas= float (input("ingrese el valor de las horas trabajas: Q"))
resultado = horas_trabajadas * costo_horas
print("el pago al trabajador es de: Q", resultado)
