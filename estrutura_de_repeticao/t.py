# """
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.
# """
# 
# termos = int(input("Digite o numero de termos da série de Fibonacci: "))
# print(type(termos))
# numero = 1
# numero_anterior = 0
# for _ in range(termos):
#     print(numero)
#     aux = numero #aux=5
#     numero += numero_anterior#numero=8
#     numero_anterior = aux#numero_anterior=5

import os 
os.system('cls')
frutas=[1,2,3,4]

for i in range(0,3):
    frutas.append(i+1)
    print(frutas)