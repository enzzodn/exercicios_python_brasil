#Q.1 Faça um Programa que peça dois números e imprima o maior deles.

import os 
os.system('cls')

print("Digite dois numeros abaixo: ")
num1=input("N1: ")
num2=input("N2: ")

if num1>num2:
    print("o maior numero eh: "+str(num1))
elif num2>num1:
    print("o maior numero eh: "+str(num2))
else:
    print("o maior numero eh: "+str(num1))