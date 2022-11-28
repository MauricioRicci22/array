C=[]
conta=0
prome=0
Cant=int(input("Cuántos medidas de temperatura va a asignar? "))

for i in range (0, Cant):
    Temp=int(input("Temperatura: "))
    prome+=Temp
    C.append(Temp)

prome=prom/Cant

for i in range (0, Cant):
    if (C[i]>=prome):
        cont+=1

print(C)
print("Hay",cont,"mayores o iguales a la temperatura media")
