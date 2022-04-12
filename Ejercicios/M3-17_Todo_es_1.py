c0=int(input("Ingresa un número positivo mayor a 0: "))

while True:
    if(c0%2==0):
        c0/=2
    else:
        c0=3*c0+1
    if c0==1:
        print("Es 1")
        break