"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem."""

import os 
os.system('cls')

print("---------------------------------")
print("-------- BASE E EXPOENTE --------")
print("---------------------------------\n")

base=int(input("Digite a base: "))
expo=int(input("Digite o expoente: "))
print("\n------------------------------------------\n")
teste=1
base1=1
if ((base > 0) or (base < 0)) and (expo > 0):
    while (teste <= expo):
        teste=teste+1
        base1=base1*base
    print("seu valor final eh: " + str(base1) + "\n")
elif (base == 0):
    print("Seu valor final eh: 0\n")
elif (expo == 0):
    print("Seu valor final eh: 1\n")