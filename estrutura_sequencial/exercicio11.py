#Q.11 Faça um Programa que peça 2 números inteiros e um número real (x,y,z). Calcule e mostre:

# a. o produto do dobro do primeiro com metade do segundo.
#   (2x * y/2)
# b. a soma do triplo do primeiro com o terceiro.
#   (3x + z)
# c. o terceiro elevado ao cubo.
#   (z^3)

import os 
os.system('cls')

print("---------------------------------------------")
print("----------- CALCULADORA ALGEBRICA -----------")
print("---------------------------------------------")

print("Digite 3 numeros, 2 inteiros e 1 real")

x=int(input("X: "))
y=int(input("Y: "))
z=float(input("Z: "))

print("--------------------")

print("Essas sao as equacoes que serao exexutadas: \n")

print("A. (2x * y/2)")
a= ((2*x)*(y/2))
print("B. (3x + z)")
b = ((3*x)+z)
print("C. (z^3) \n")
c = (z*z*z)

print("-------------------- \n")

print("------- RESULTADOS -------")
print("A: "+str(a))
print("B: "+str(b))
print("C: "+str(c))