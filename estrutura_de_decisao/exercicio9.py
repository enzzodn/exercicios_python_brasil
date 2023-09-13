# Q.9 Faça um Programa que leia três números e mostre-os em ordem decrescente.

import os 


os.system('cls')

print("---------------------------------------")
print("---------- ORDEM DECRESCENTE ----------")
print("---------------------------------------")

print("Digite abaixo 3 numeros e os colocarei em ordem decrescente: ")
n1=input("N1: ")
n2=input("N2: ")
n3=input("N3: ")
print("------------- \n")

if n1>=n2 and n1>=n3:
    maior=n1
elif n2>=n1 and n2>=n3:
    maior=n2
elif n3>=n1 and n3>=n2:
    maior=n3

if n1<n2 and n1<n3:
    menor=n1
elif n2<n1 and n2<n3:
    menor=n3 
elif n3<n1 and n3<n2:
    menor=n3

if n1>n2 and n1<n3 or n1<n2 and n1>n3:
    meio=n1
elif n2>n1 and n2<n3 or n2<n1 and n2>n3:
    meio=n2
elif n3>n1 and n3<n2 or n3<n1 and n3>n2:
    meio=n3

# if n2>n1>n3 or n3>n1>n2:
#     meio=n1
# elif n1>n2>n3 or n3>n2>n1:
#     meio=n2
# elif n1>n3>n2 or n2>n3>n1:
#     meio=n3


print("Ordem decrescente: " + str(maior) + ", " + str(meio) + ", " + str(menor))
