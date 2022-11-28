import random

lista=[]

cant=int(input("Cantidad de numeros: "))

for i in range (0, cant):
    nume=random.randint(1,100)
    lista.append(num)

lista.sort()
nume=0

for i in range (0, cant):
    if (lista[i]>nume):
        print(lista[i])
        nume=lista[i]
