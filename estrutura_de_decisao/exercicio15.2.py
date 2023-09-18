"""Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

import os 
import random
os.system('cls')

print("----------------------------------------")
print("----------- EH UM TRIANGULO? -----------")
print("---------------------------------------- \n")

print("Informe abaixo 3 valores para cada lado de um triangulo:")
l1=random.randrange(0,20)
l2=random.randrange(0,20)
l3=random.randrange(0,20)

print("Lado1: " + str(l1))
print("Lado2: " + str(l2))
print("Lado3: " + str(l3))
print("-------------------------------------------------------------- \n")

# --------------- MAIOR ---------------
if (l1 > l2) and (l1 > l3):
    maior=l1
elif (l2 > l1) and (l2 > l3):
    maior=l2 
elif (l3 > l1) and (l3 > l2):
    maior=l3
else:
    maior=l1

# --------------- MENOR ---------------
if (l1 < l2) and (l1 < l3):
    menor=l1 
elif (l2 < l1) and (l2 < l3):
    menor=l2 
elif (l3 < l1) and (l3 < l2):
    menor=l3
else:
    menor=l1

# --------------- MEIO ---------------
if ((l1 < l2) and (l1 > l3)) or ((l1 > l2) and (l1 < l3)):
    meio=l1 
elif ((l2 > l1) and (l2 < l3)) or ((l2 < l1) and (l2 > l3)):
    meio=l2 
elif ((l3 > l1) and (l3 < l2)) or ((l3 < l1) and (l3 > l2)):
    meio=l3
else:
    meio=l1

# ---------- CONDICAO DE EXISTENCIA -----------
if (maior < (menor + meio)):
    print("Eh um triangulo? SIM")
else:
    print("Eh um triangulo? NAO")

# ---------------- TIPOS ------------------
if (l1 == l2) and (l1 == l3):
    print("O seu triangulo eh do tipo: EQUILATERO")
    # 1 1 0 / 1 0 1 / 0 1 1
elif ((l1 == l2) and (l3 != l1)) or ((l1 == l3) and (l2 != l1)) or ((l3 == l2) and (l3 != l1)):
    print("O seu triangulo eh do tipo: ISOSCELES")
elif (l1 != l2) and (l1 != l3) and (l2 != l3):
    print("O seu triangulo eh do tipo: ESCALENO")