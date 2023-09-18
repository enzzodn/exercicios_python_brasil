"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

* Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o
programa não deve fazer pedir os demais valores, sendo encerrado;
* Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;
* Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
* Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

import os 
os.system('cls')

print("------------------------------------------------------------------------")
print("-------------------- EQUACAO DO SEGUNDO GRAU (DELTA)--------------------")
print("------------------------------------------------------------------------ \n")

print("FORMULA 1: ax² + bx + c")
print("FORMULA 2: Δ = b² -4ac")
print("FORMULA 3: X = (-b ± √Δ) / 2a \n")
print("Digite abaixo os valores de 'a', 'b' e 'c' respectivamente:")

a=int(input("A: "))

if (a == 0):
    print("Seu valor de 'A' eh 0, equação não é do segundo grau")
    print("Portanto nao ha como calcular")
    exit() # 'exit()' para o programa

b=int(input("B: "))
c=int(input("C: "))
print("------------------------- \n")

delta = (b * b) - 4 * (a * c)
x1 = (-b + (delta ** 1/2)) / (2 * a)
x2 = (-b - (delta ** 1/2)) / (2 * a)

if (delta > 0):
    print("O valor de 'delta' eh POSITIVO, portanto:")
    print("A equação possui duas raiz reais")
    print("-----------")
    print("Raiz 1: " + str(x1))
    print("Raiz 2: " + str(x2))
elif (delta < 0):
    print("O valor de 'delta' eh NEGATIVO, portanto:")
    print("A equação não possui raizes reais")
elif (delta == 0):
    print("O valor de 'delta' eh IGUAL A ZERO, portanto:")
    print("A equação possui apenas uma raiz real")
    print("-----------")
    print("Raiz 1 e 2: " + str(x1))