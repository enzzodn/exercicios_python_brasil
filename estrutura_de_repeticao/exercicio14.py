"""Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares."""

import os 
os.system('cls')
print("---------------------------------")
print("-------- PARES E IMPARES --------")
print("---------------------------------\n")
teste=1
par=0
impar=0
print("Digite 10 numeros e lhe mostrarei a quantidade de pares e impares\n")
while (teste <= 10):
    n=int(input("Digite o "+str(teste)+"º numero: "))
    if (n % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1
    teste = teste + 1
print("\n--------------------------------\n")
print("Qntd. pares: "+ str(par))
print("Qntd. impares: " + str(impar)+"\n")