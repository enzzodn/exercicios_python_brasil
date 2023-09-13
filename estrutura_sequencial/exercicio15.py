"""
Q.15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato (5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido
"""

import os 
os.system('cls')

print("--------------------------------------------------------")
print("------------ CALCULADORA DE SALARIO LIQUIDO ------------")
print("--------------------------------------------------------")

gh=input("Digite aqui quanto voce ganha por hora: ")
nh=input("Digite aqui a quant. de horas que voce trabalha por mes: ")
sb=float(gh)*int(nh)
print("-------------------- \n")
print("Salario bruto: R$ "+str(sb)+"\n")

print("-------------------- \n")
print("---------- DESCONTOS ----------")
print("IR (11%)")
ir=sb*11/100
print("INSS (8%)")
inss=sb*8/100
print("Sindicato (5%) \n")
sind=sb*5/100

print("-------------------- \n")
print("Seus descontos foram calucalos: ")
print("IR (11%): R$ "+str(ir))
print("INSS (8%): R$ "+str(inss))
print("Sindicato (5%): R$ "+str(sind)+"\n")

print("-------------------- \n")
sl=sb-ir-inss-sind
print("Portanto seu salario liquido ficara em: R$ "+str(sl))