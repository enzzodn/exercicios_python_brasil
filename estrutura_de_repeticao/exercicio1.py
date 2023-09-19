"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

import os 
os.system('cls')

print("digite um numero entre 0 e 10")
num=float(input("N: "))

while True:
    if (num >= 0) and (num <= 10):
        print("VALOR VALIDO")
        break 
    else:
        print("VALOR INVALIDO")
        print("Por favor, digite novamente \n")
        num=float(input("N: "))