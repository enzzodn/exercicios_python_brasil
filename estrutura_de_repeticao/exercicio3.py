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

# ------ PARTE 1 (NOME) -----------
nome=input("NOME: ")

quantnome= len(nome)
while (quantnome < 3):
    if True:
        print("Seu nome deve ter mais de 3 caracteres!")
        print("Por favor, digite novamente.")
    nome=input("NOME: ")
    quantnome= len(nome)

os.system('cls')
print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")
print("Digite abaixo os dados que se pedem: ")

print("NOME: " + nome)

# ------ PARTE 2 (IDADE) -----------
idd=int(input("IDADE: "))

while (idd < 0) or (idd > 150):
    if True:
        print("Sua idade deve ser entre 0 e 150 anos!")
        print("Por favor, digite novamente.")
    idd=int(input("IDADE: "))
    break


os.system('cls')
print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")
print("Digite abaixo os dados que se pedem: ")

print("NOME: " + nome)
print("IDADE: "+ str(idd))

# ------ PARTE 3 (SALÁRIO) -----------

sal=float(input("SALARIO: "))
sexo=input("SEXO ('m' ou 'f'): ")
ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")

# -------- CONDIÇÕES --------------

    
