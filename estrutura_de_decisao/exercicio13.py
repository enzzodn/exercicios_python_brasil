# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

import os 
os.system('cls')

print("digite um numero entre 1 e 7 e diremos o dia da semana correspondente: \n")
n=int(input("N: "))

if (n == 1):
    n = "1 - Domingo"
elif (n == 2):
    n="2 - Segunda-Feira"
elif (n == 3):
    n="3 - Terça-Feira"
elif (n == 4):
    n="4 - Quarta-Feira"
elif (n == 5):
    n="5 - Quinta-Feira"
elif (n == 6):
    n="6 - Sexta-Feira"
elif (n == 7):
    n="7 - Sabado"
else:
    n="valor invalido"

print("Voce escolheu: " + n)