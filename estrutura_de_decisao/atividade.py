"""
a. Faça um programa que recebe o salário de um colaborador e
    o reajuste segundo o seguinte critério, baseado no salário atual;
b. Salários até R$ 280,00 (incluindo): aumento de 20%;
c. Salários entre R$ 280,00 e R$700,00: aumento de 15%;
d. Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
e. Salários de R$ 1500,00 em diante: aumento de 5%

Após o aumento ser realizado; informe na tela;

a. O salário antes do reajuste;
b. O percentual de aumento aplicado;
c. O valor do aumento;
d. O novo salário, após o aumento.
"""

import os 
os.system('cls')

print("-------------------------------------\n")
print("----------- A U M E N T O -----------\n")
print("-------------------------------------\n\n")

print("Digite abaixo valor do seu salario atual: \n")
sal=float(input("R$ "))

if (sal <= 280):
    aumento = sal * 20/100
    salaj = sal + aumento
    prcnt="20%"
elif (sal > 280) and (sal <= 700):
    aumento = sal * 15/100
    salaj = sal + aumento
    prcnt="15%"
elif (sal > 700) and (sal <= 1500):
    aumento = sal * 10/100
    salaj = sal + aumento
    prcnt="10%"
elif (sal > 1500):
    aumento = sal * 5/100
    salaj = sal + aumento
    prcnt="5%"

print("\n------------------------------\n")
print("--------- FINANCEIRO ---------\n\n")

print("Salario anterior: " + str(sal) + "\n")
print("Porcentual aplicado: " + str(prcnt) + "\n")
print("Valor aumentado: " + str(aumento) + "\n\n")
print("------------------------------\n")
print("SALARIO ATUAL: " + str(salaj) + "\n")