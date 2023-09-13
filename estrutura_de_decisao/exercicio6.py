# Q.6 Faça um Programa que leia três números e mostre o maior deles.

import os
import random


os.system('cls')

print("----------------------------------")
print("---------- MAIOR NUMERO ----------")
print("----------------------------------")

print("Abaixo, 3 numeros, irei adivinhar o maior entre eles: ")
n1=random.randrange(0,100)
n2=random.randrange(0,100)
n3=random.randrange(0,100)

print("N1: "+str(n1))
print("N2: "+str(n2))
print("N3: "+str(n3))

print("---------------- \n")

if n1>n2 and n1>n3:
    print("O maior eh: "+str(n1))
elif n2>n1 and n2>n3:
    print("O maior eh: "+str(n2))
elif n3>n1 and n3>n2:
    print("O maior eh: "+str(n3))
