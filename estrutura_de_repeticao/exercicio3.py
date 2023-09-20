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

print("Digite abaixo os dados que se pedem: \n")
nome=input("NOME: ")
idd=int(input("IDADE: "))
sal=float(input("SALARIO: "))
sexo=input("SEXO ('m' ou 'f'): ")
ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")

# ------ NOME ------
quantnome = len(nome)
while (quantnome < 3):
    print("---------------------------- \n")
    print(" ------- ATENCAO ------- ")
    print("Seu nome deve ter mais de 3 caracteres!")
    print("Por favor, digite novamente.")
    teste=nome
    break

# ------ IDADE ------
while (idd < 0) or (idd > 150):
    print("---------------------------- \n")
    print(" ------- ATENCAO ------- ")
    print("Sua idade deve ser entre 0 e 150 anos!")
    print("Por favor, digite novamente.")
    teste=idd
    break

# ------ SALARIO ------
while (sal <= 0):
    print("---------------------------- \n")
    print(" ------- ATENCAO ------- ")
    print("Seu salario deve ser maior que 0!")
    print("Por favor, digite novamente.")
    teste=sal
    break

# ------ SEXO ------
while (sexo != "m") and (sexo != "f"):
    print("---------------------------- \n")
    print(" ------- ATENCAO ------- ")
    print("Seu sexo deve ser definido somente em 'm' ou 'f'!")
    print("Por favor, digite novamente.")
    teste=sexo
    break

# ------ ESTADO CIVIL ------
while (ec != "s") and (ec != "c") and (ec != "v") and (ec != "d"):
    print("---------------------------- \n")
    print(" ------- ATENCAO ------- ")
    print("Seu estado civil deve ser: 's', 'c', 'v' ou 'd'!")
    print("Por favor, digite novamente.")
    teste=ec
    break   

# FUNCIONALIDADE



teste=nome
teste=idd 
teste=sal 
teste=sexo 
teste=ec

# PRA DAR ERRADO



# PRA DAR CERTO

"""if (teste == nome) or (teste == idd) or (teste == sal) or (teste == sexo) or (teste == ec):
    print("   ")
    exit()
elif (teste != nome) or (teste != idd) or (teste != sal) or (teste != sexo) or (teste != ec):
    print("   ")
    exit()

if (teste == nome) and (teste == idd) and (teste == sal) and (teste == sexo) and (teste == ec):
    print("---------------------------- \n")
    print("Seus dados pessoais atendem todos os nossos requisitos!")
    print("Aguarde e voce sera redirecionado para outra pagina.")
    print(" ")
elif (teste != nome) and (teste != idd) and (teste != sal) and (teste != sexo) and (teste != ec):
    print("---------------------------- \n")
    print("Seus dados pessoais atendem todos os nossos requisitos!")
    print("Aguarde e voce sera redirecionado para outra pagina.")
    print(" ")"""