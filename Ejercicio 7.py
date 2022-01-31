#Ejercicio 7: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso = float(input("Ingrese la masa en kg de la persona: "))
estatura = float(input("Ingrese la estatura en m de la persona: "))
indice = round(float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal (IMC) de la persona es de: "+ str(indice))