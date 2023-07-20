print("Ingrese los valores de las ecuaciones cuadriticas")
A = int(input("A :"))
B = int(input("B :"))
C = int(input("C :"))
D = B**2 - 4*A*C

if D > 0:
    x1 =  ( (-B) - D**0.5)/ 2*A
    x2 =  ( (-B) - D**0.5)/ 2*A
    print("Raices reales", x1,x2,)
else:
    print("raices irracionales")
