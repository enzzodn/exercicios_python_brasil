"""Faça um programa que leia e valide as seguintes informações:
* Nome: maior que 3 caracteres;
* Idade: entre 0 e 150;
* Salário: maior que zero;
* Sexo: 'f' ou 'm';
* Estado Civil: 's', 'c', 'v', 'd';"""

import os 
os.system('cls')

print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")

print("Digite abaixo os dados que se pedem: ")
nome=input("NOME: ")
while (nome < "   "):
    print("Seu nome deve ter no minino 3 caracteres!")
    print("Por favor, digite novamente!")
    break

idd=int(input("IDADE: "))
idade=int((idd>=0)and(idd<=150))
while (idd != idade):
    print("Sua idade deve ser entre 0 e 150!")
    print("Por favor, digite novamente!")
    break

sal=input("SALARIO: ")
sexo=input("SEXO ('m' ou 'f'): ")
ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")