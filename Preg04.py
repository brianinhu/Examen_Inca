print("Datos de entrada: ")
#Ingresar el valor de la ganancia
ganancia = float(input("Ganancia: "))

#Condicional para hallar el valor de la donacion según el valor de ganancia
if ganancia >= 0 and ganancia <= 1000:
    donacion = ganancia*0.05
elif ganancia >= 1001 and ganancia <= 1500:
    donacion = ganancia*0.07
elif ganancia >=1501 and ganancia <= 2000:
    donacion = ganancia*0.08
elif ganancia >= 2001 and ganancia <= 5000:
    donacion = ganancia*0.1
elif ganancia >= 5001:
    donacion = ganancia*0.15

#Imprimir el valor de la donación
print("\nDatos de salida: ")
print(f"Donación: S/.{donacion}")