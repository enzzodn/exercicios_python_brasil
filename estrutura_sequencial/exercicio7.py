#Q.7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

import os 
os.system('cls')

print("-------------------------------------------------------")
print("---------- DOBRO DA AREA DE UM QUADRADO ---------------")
print("-------------------------------------------------------")

l=input("Digite o valor (inteiro) do lado de um quadrado: ")
a=int(l)*int(l)

print("---------------")
doba=2*a
print("A area dese quadrado eh: "+str(a)+" | e seu dobro eh de: "+str(doba))