#Q6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#(A = π r²) -- Área do círculo

import os
os.system('cls')

print("--------------------------------------")
print("----------- area do circulo ----------")
print("-------------------------------------- \n")

r=input("Digite aqui o raio do circulo: ")
a= 3.14*int(r)*int(r)

print("----------")
print("A area do circulo eh de: aprox. "+str(a)+"cm²")