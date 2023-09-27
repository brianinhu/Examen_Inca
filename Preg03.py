print("Datos de entrada: ")
#Ingresar el valor de las horas
horas = float(input("Horas: "))

#Condicional para hallar el importe según las horas de estacionamiento
if horas < 5:
    importe = 6
else:
    importe = 6 + ((horas-4)*2)

#Imprimir el importe total
print("\nDatos de salida: ")
print(f"Importe a pagar: S/.{importe}")