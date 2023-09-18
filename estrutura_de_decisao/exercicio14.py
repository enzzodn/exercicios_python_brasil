"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

import os 
os.system('cls')

print('-----------------------------------------------')
print("--------------- MEDIA SEMESTRAL ---------------")
print('-----------------------------------------------')

print("Sua nota final vai ser baseada nessa tabela: \n")
print("Média de Aproveitamento | Conceito")
print("   Entre 9.0 e 10.0     |     A")
print("   Entre 7.5 e 9.0      |     B")
print("   Entre 6.0 e 7.5      |     C")
print("   Entre 4.0 e 6.0      |     D")
print("   Entre 4.0 e zero     |     E \n")

print("----------------------------------------------- \n")

print("Digite a nota do seu 1º Bim. :")
b1=float(input("Bim.1: "))
print("Digite a nota do seu 2º Bim. :")
b2=float(input("Bim.2: "))

print("----------------------------------------------- \n")

# ------------ FORMULA - IF/ELSE ---------------
m = (b1+b2)/2

if (m >= 9) and (m <= 10):
    print("Sua media foi de: " + str(m))
    print("Nota A - APROVADO(A)")
elif (m >= 7.5) and (m < 9):
    print("sua media foi de: "+ str(m))
    print("Nota B - APROVADO(A)")
elif (m >= 6) and (m < 7.5):
    print("sua media foi de: "+ str(m))
    print("Nota C - APROVADO(A)")
elif (m >= 4) and (m < 6):
    print("sua media foi de: "+ str(m))
    print("Nota D - REPROVADO(A)")
elif (m >= 0) and (m < 4):
    print("sua media foi de: "+ str(m))
    print("Nota E - REPROVADO(A)")