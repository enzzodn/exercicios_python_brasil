"""Faça um Programa que leia 2 números e em seguida pergunte ao
usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
* par ou ímpar;
* positivo ou negativo;
* inteiro ou decimal.
"""

import os 
os.system('cls')

print("-----------------------------------")
print("----------- CALCULADORA -----------")
print("----------------------------------- \n")

print("--- TABELA DE OPERAÇÕES ---")
print("[1] SOMA")
print("[2] SUBTRACAO")
print("[3] MULTIPLICACAO")
print("[4] DIVISAO")
print("[5] POTENCIACAO")
print("--------------------------- \n")

print("Digite abaixo 2 numeros")
n1=float(input("N1: "))
n2=float(input("N2: "))
print(" \n")

print("Agora digite o numero correspondente da operacao")
op=int(input("OP: "))
if (op != 1) and (op != 2) and (op != 3) and (op != 4) and (op != 5):
    print("OPERACAO INVALIDA")
    exit()

print("-------------------\n")

if (op == 1):
    res=n1+n2
    print("O resultado da sua SOMA eh: " + str(res) + "\n")
elif (op == 2):
    res=n1-n2
    print("O resultado da sua SUBTRACAO eh: " + str(res) + "\n")
elif (op == 3):
    res=n1*n2
    print("O resultado da sua MULTIPLICACAO eh: " + str(res) + "\n")
elif (op == 4):
    res=n1/n2 
    print("O resultado da sua DIVISAO eh: " + str(res) + "\n")
elif (op == 5):
    res=n1**n2 
    print("O resultado da sua POTENCIACAO eh: " + str(res) + "\n")

print("-------------------\n")

if (res % 2 == 0):
    print("Seu numero eh PAR\n")
else:
    print("Seu numero eh IMPAR\n")

if (res >= 0):
    print("Seu numero eh POSITIVO\n")
else:
    print("Seu numero eh NEGATIVO\n")

"""    if (res % 2 == 0):
        print("Seu numero eh INTEIRO")
    else:
        print("Seu numero eh DECIMAL")"""