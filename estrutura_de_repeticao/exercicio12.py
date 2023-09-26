"""Desenvolva um gerador de tabuada, capaz de gerar
a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50"""

import os
os.system('cls')

print("-------------------------------")
print("----------- TABUADA -----------")
print("------------------------------- \n")

n=int(input("Escolha um numero de 1 a 10: "))
cont=1
print("-----------------------------\n")
if (n >= 1) and (n <= 10):
    while (cont <= 10):
        res=n*cont
        print(str(n) + " * " + str(cont) + " = " + str(res))
        cont = cont + 1
elif (n > 10) or (n < 1):
    print("Voce deve escolher somente os numeros de 1 a 10!")  