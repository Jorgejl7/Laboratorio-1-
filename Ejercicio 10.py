#Ejercicio 10:Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
peso_payaso = 112
peso_muñeca = 75

payaso = int(input("Ingrese el total de payasos vendidos: "))
muñeca = int(input("Ingrese el total de muñecas vendidos: "))

total_peso = peso_payaso * payaso + peso_muñeca * muñeca

print("El peso total del paquetes es de: " + str(total_peso) + "g")