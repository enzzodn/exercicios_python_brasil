"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo."""

import os 
os.system('cls')
print("-----------------------------------------")
print("--------------- FIBONACCI ---------------")
print("----------------------------------------- \n")

print("A serie de Fibonacci é formada pela sequencia 0,1,1,2,3,5,8,13,21,34,55,...\n")
print("----------------------------------\n")

pos=int(input("POSICAO: "))
print("\n----------------------------------\n")
n=1
num=0
for _ in range(pos):
    print(num)
    
