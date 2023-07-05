ganado=int(input("Cuantos partidos ganados"))
empatado=int(input("cuantos partidos empatados"))
perdido=int(input("cuantos partidos perdidos"))

a=ganado*3
b=empatado+1
c=perdido-1
total= a+b-c
print ("los partidos ganados suman", a)
print ("los partidos empatados suman", b)
print("los partidos perdidos restas", c)

print ("los puntos finales son", total)
