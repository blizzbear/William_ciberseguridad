from Crypto.Util import number
import random

#ejercicio 1
print("ejercicio 1 numero aleatorio de 256 bits", random.getrandbits(1024),"\n")

#ejercicio 2
i=0
while(True):
  i=i+1
  j= random.getrandbits(1024)
  esPrimo= number.isPrime(j)
  if(esPrimo):
    print("numero primo", j, "intento", i, "\n")
    break



#ejercicio 3

def inversoMultiplicativo(x,y):
  print("Ejercicio 3 - El inverso multiplicativo del numero x:", "\n", "y el numero y:","\n", number.inverse(x,y), "\n")


a= random.getrandbits(1024)
b= random.getrandbits(1024)
inversoMultiplicativo(a,b)

#ejercicio 4

a=2
b= random.getrandbits(256)
c= j

def potencia(x,y,z):
  
  print("Ejercicio 4 - La potencia de x elevado a y modulo z:", "\n", pow(x,y,z))


potencia(a,b,c)








  


    
    

