from distutils.log import error


Matr=[]

size=int(input("ingrese tamaño de la matriz cuadrada: "))

for i in range (0,size):
    Matr.append([])
    for j in range (0,size):
        Matr[i].append(int(input()))

for i in range (0,size):
    Matr.append([])
    for j in range (0,size):
        if (Matr[i][j]!=Matr[j][i]):
            print("la matriz no es simetrica!")
            print("error")
            error=0/0

print("Matriz simetrica!")
for i in range(0,size):
    print(Matr[i])
