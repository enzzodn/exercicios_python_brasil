"""
Q.5 Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
b. A mensagem "Reprovado", se a média for menor do que sete;
c. A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

import os 


os.system('cls')

print("--------------------------")
print("-------- PASSOU?? --------")
print("-------------------------- \n")

print("Digite abaixo suas notas (P1 e P2):")
p1=int(input("P1: "))
p2=int(input("P2: "))
print("--------------")

m=(p1+p2)/2
print("Sua media: "+str(m)+"\n")
print("--------------")

if m>=7:
    print("Voce esta APROVADO")
elif m<7:
    print("Voce esta REPROVADO")
elif m == 10:
    print("Voce esta APROVADO COM DISTINCAO")
