# Q.6 Faça um Programa que leia três números e mostre o maior deles.

import os


os.system('cls')

print("----------------------------------")
print("---------- MAIOR NUMERO ----------")
print("----------------------------------")

print("Digite abaixo 3 numero e irei adivinhar o maior entre eles: ")

n1=input("N1: ")
n2=input("N2: ")
n3=input("N3: ")
print("---------------- \n")

if n1>=n2 and n1>=n3:
    print("O maior eh: "+str(n1))
elif n2>=n1 and n2>=n3:
    print("O maior eh: "+str(n2))
elif n3>=n1 and n3>=n2:
    print("O maior eh: "+str(n3))
