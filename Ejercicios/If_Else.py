ingreso=float(input("Ingrese el ingreso anual:"))

if (ingreso<0):
    impuesto=0
elif (ingreso<85528):
    impuesto=0.18*ingreso-556.2
else:
    impuesto=14839.2+0.32*(ingreso-85.528)
    
impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
