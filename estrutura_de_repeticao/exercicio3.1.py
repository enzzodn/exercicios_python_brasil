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
    print("Sua idade deve ser entre 0 e 150 anos!")
    print("Por favor, digite novamente.")
    idd=int(input("IDADE: "))
    
os.system('cls')
print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")
print("Digite abaixo os dados que se pedem: ")

print("NOME: " + nome)
print("IDADE: "+ str(idd))

# ------ PARTE 3 (SALÁRIO) -----------

sal=float(input("SALARIO: "))

while (sal <= 0):
    print("Seu salario deve ser maior que 0!")
    print("Por favor, digite novamente.")
    sal=float(input("SALARIO: "))

os.system('cls')
print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")
print("Digite abaixo os dados que se pedem: ")

print("NOME: " + nome)
print("IDADE: "+ str(idd))
print("SALARIO: R$ "+ str(sal))

# ------ PARTE 4 (SEXO) -----------

sexo=input("SEXO ('m' ou 'f'): ")

if (sexo == "m") or (sexo == "M"):
    sexo = "Masculino"
elif (sexo == "f") or (sexo == "F"):
    sexo = "Feminino"

while (sexo != "Masculino") and (sexo != "Feminino"):
    print("Seu sexo deve ser definido somente com 'm' ou 'f'!")
    print("Por favor, digite novamente.")
    sexo=input("SEXO ('m' ou 'f'): ")
    if (sexo == "m") or (sexo == "M"):
        sexo = "Masculino"
    elif (sexo == "f") or (sexo == "F"):
        sexo = "Feminino"

os.system('cls')
print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")
print("Digite abaixo os dados que se pedem: ")

print("NOME: " + nome)
print("IDADE: "+ str(idd))
print("SALARIO: R$ "+ str(sal))
print("SEXO: "+ sexo)

# ------ PARTE 5 (ESTADO CIVIL) -----------

ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")

if (ec == "s") or (ec == "S"):
    ec = "Solteiro(a)"
elif (ec == "c") or (ec == "C"):
    ec = "Casado(a)"
elif (ec == "v") or (ec == "V"):
    ec = "Viuvo(a)"
elif (ec == "d") or (ec == "D"):
    ec = "Divorciado(a)"

while (ec != "Solteiro(a)") and (ec != "Casado(a)") and (ec != "Viuvo(a)") and (ec != "Divorciado(a)"):
    print("Seu estado civil deve ser: 's', 'c', 'v' ou 'd'!")
    print("Por favor, digite novamente.")
    ec=input("ESTADO CIVIL ('s', 'c', 'v' ou 'd'): ")
    if (ec == "s") or (ec == "S"):
        ec = "Solteiro(a)"
    elif (ec == "c") or (ec == "C"):
        ec = "Casado(a)"
    elif (ec == "v") or (ec == "V"):
        ec = "Viuvo(a)"
    elif (ec == "d") or (ec == "D"):
        ec = "Divorciado(a)"

os.system('cls')
print("----------------------------------------")
print("------------ DADOS PESSOAIS ------------")
print("---------------------------------------- \n")
print("Digite abaixo os dados que se pedem: ")

print("NOME: " + nome)
print("IDADE: "+ str(idd))
print("SALARIO: R$ "+ str(sal))
print("SEXO: "+ sexo)
print("ESTADO CIVIL: "+ ec)

print("------------------------------- \n")
print("Seus dados pessoais atendem todos os nosso requisitos!")
print("Auarde um momento e voce ja sera direcionado para outra pagina.")
print(" ")