bloques = int(input("Ingrese el número de bloques:"))
i=1
altura=0
while True:
    if bloques-i>=0:
        bloques-=i
        i+=1
        altura+=1
    else:
        break
print("La altura de la pirámide:", altura)