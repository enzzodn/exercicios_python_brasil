#Q.2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

import os 


os.system('cls')

print("--------------------------------")
print("--------- PAR OU IMPAR ---------")
print("--------------------------------")

num=float(input("Digite um numero e verifique se ele eh par ou impar: \n"))
print("-----------------")

if num%2 == 0:
    print("Seu numero eh PAR")
else:
    print("Seu numero eh IMPAR")
    