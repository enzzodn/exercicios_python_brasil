"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

import os 
os.system('cls')

print("---------------------------")
print("-------- INSTAGRAM --------")
print("--------------------------- \n")


nome=input("NOME: ")
senha=input("SENHA: ")
os.system('cls')
while True:
    if (senha != nome):
        print("---------------------------")
        print("-------- INSTAGRAM --------")
        print("--------------------------- \n")
        print("ACESSO LIBERADO")
        break
    else:
        print("---------------------------")
        print("-------- INSTAGRAM --------")
        print("--------------------------- \n")
        print("Senha nao pode ser igual ao nome!")
        print("Por favor, digite suas informacoes novamente: \n")
        nome=input("NOME: ")
        senha=input("SENHA: ")
        os.system('cls')

    