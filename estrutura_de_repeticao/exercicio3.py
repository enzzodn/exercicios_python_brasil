"""Faça um programa que leia e valide as seguintes informações:
* Nome: maior que 3 caracteres;
* Idade: entre 0 e 150;
* Salário: maior que zero;
* Sexo: 'f' ou 'm';
* Estado Civil: 's', 'c', 'v', 'd';
"""

import os 
os.system('cls')

print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")

print("Digite abaixo os dados que se pedem: ")
nome=input("NOME: ")

# ------- NOME -------
if (nome >= '   '):
        nome=nome
else:
    print("----------------------------------------")
    print("------------ DADOS PESSOAIS ------------")
    print("---------------------------------------- \n")

    print("Seu nome esta com menos de 3 caracteres!")
    print("Por favor, rescreva-o novamente: \n")
    nome=input("NOME: ")
    idd=int(input("IDADE: "))
    sal=float(input("SALARIO: "))
    sexo=input("SEXO ('f' ou 'm'): ")
    ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")
    print("----------------------------------------- \n")

idd=int(input("IDADE: "))

# ------ IDADE -------
if (idd >= 0) and (idd <= 150):
    idd=idd
else:
    print("Sua idade deve ser entre 0 e 150 anos!")
    print("Por favor, rescreva-a novamente: \n")
    idd=int(input("IDADE: "))
    sal=float(input("SALARIO: "))
    sexo=input("SEXO ('f' ou 'm'): ")
    ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")
    print("----------------------------------------- \n")

sal=float(input("SALARIO: "))

# -------- SALARIO -------
if (sal > 0):
    sal=sal
else:
    print("Seu salario deve ser maior que 0!")
    print("Por favor, rescreva-o novamente: \n")
    sal=float(input("SALARIO: "))
    sexo=input("SEXO ('f' ou 'm'): ")
    ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")
    print("----------------------------------------- \n")

sexo=input("SEXO ('f' ou 'm'): ")

# ------ SEXO ------
if (sexo == "f") or(sexo == "m"):
    sexo=sexo 
else:
    print("Seu sexo deve ser 'f' ou 'm'!")
    print("Por favor, rescreva-o novamente: \n")
    sexo=input("SEXO ('f' ou 'm'): ")
    ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")
    print("----------------------------------------- \n")

ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")

# --------- ESTADO CIVIL ----------
if (ec == "s")or (ec == "c") or (ec == "v") or (ec == "d"):
    ec=ec
else:
    print("Seu estado civil deve ser escrito somente como: 's', 'c', 'v' ou 'd'!")
    print("Por favor, rescreva-o novamente: \n")
    ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")
    print("----------------------------------------- \n")

print("----------------------------------------- \n")
print("Todos os seus dados atendem nossos requisitos!")
print("Obrigado pela confiança! Até logo!")