print("Ingrese el año")
A = int(input())
print ("ingrese el mes")
B = int(input())
print ("ingrese el dia")
C = int(input())
if C>0 and B <30:
    C+1
    print("Mañana es: ",C+1,B,A,)
else:
 if B > 0 and B < 12 :
    print("Mañana es:", 1, B+1, A)
 else:
   print("Mañana es:", 1, 1, A+1)
    