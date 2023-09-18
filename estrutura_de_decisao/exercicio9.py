# Q.9 Faça um Programa que leia três números e mostre-os em ordem decrescente.

import os 
os.system('cls')

print("-----------------------------------------")
print("----------- ORDEM DECRESCENTE -----------")
print("----------------------------------------- \n")

print("Digite 3 numeros: \n")
n1=int(input("N1: "))
n2=int(input("N2: "))
n3=int(input("N3: "))

print("----------------------- \n")

# --------------- MAIOR ---------------
if (n1 > n2) and (n1 > n3):
    maior=n1
elif (n2 > n1) and (n2 > n3):
    maior=n2 
elif (n3 > n1) and (n3 > n2):
    maior=n3 

# --------------- MENOR ---------------
if (n1 < n2) and (n1 < n3):
    menor=n1 
elif (n2 < n1) and (n2 < n3):
    menor=n2 
elif (n3 < n1) and (n3 < n2):
    menor=n3 

# --------------- MEIO ---------------
if ((n1 < n2) and (n1 > n3)) or ((n1 > n2) and (n1 < n3)):
    meio=n1 
elif ((n2 > n1) and (n2 < n3)) or ((n2 < n1) and (n2 > n3)):
    meio=n2 
elif ((n3 > n1) and (n3 < n2)) or ((n3 < n1) and (n3 > n2)):
    meio=n3

# ----------- RESOLUÇÃO -------------

print("Estes sao seus numeros em ordem decrescente: " + str(maior) +" | "+ str(meio) +" | " + str(menor))