#Faça um programa que, dado um conjunto de N números,
#determine o menor valor, o maior valor e a soma dos valores.

import os 
os.system('cls')

print("------------------------------------------------------")
print("---------------- MENOR / MAIOR / SOMA ----------------")
print("------------------------------------------------------\n")

print("Voce pode digitar quantos numeros quiser")
print("E eu imprimirei o menor valor, o maior e a soma deles!!\n")

teste="s"
soma=0
maior=0
cont=0
print("------------------------------------------------------\n")

while (teste=="s") or (teste=="S") or (teste=="sim") or (teste=="Sim"):
    n=int(input("Digite um numero: "))

    if cont==0:
        menor = n
        
    soma = soma + n

    if n >= maior:
          maior = n
    if n <= menor:
        menor = n

    teste=input("Voce deseja continuar? (s/n): ")
    cont += 1
    
print(str(maior) +"  "+ str(menor) +"  "+ str(soma))