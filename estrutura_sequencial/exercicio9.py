#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

#C = 5 * ((F-32) / 9).

import os
os.system('cls')

print("-------------------------------------------")
print("----- CONVERSOR FAHRENHEIT -> CELSIUS -----")
print("------------------------------------------- \n")

f=input("Digite, em graus Fahrenheit, para ser convertido em Celsius: ")
calc=("C = 5 * ((F-32) / 9)")

print("----------------")
print("O calculo sera baseado nessa equacao: "+calc)
print("----------------")

c = 5 * ((float(f)-32) / 9)

print("Seu valor em F era: "+str(f))
print("E agora seu valor em C eh: "+str(c))