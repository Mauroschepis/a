print("Ingrese la velocidad de los vehiculos")
V1 = int(input())
v2 = int(input())
print("ingrese la distancia que los separa")
D = int(input())
if V1>0 and v2>0:
 T = D/(v2 + V1)
 print ("el tiempo de encuentro de segundos entre los vehiculos es",T )
else:
    print ("ERROR")