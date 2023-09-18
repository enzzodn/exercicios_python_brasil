# Faça um Programa que pergunte em que turno você estuda. Peça para digitar
#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

import os 
os.system('cls')

print("------------------------------- \n")
nome=input("Qual seu nome? ")
turno=input("E qual turno voce estuda? (responda V-Vespertino / M-Matutino / N-Noturno): ")

# ---------- IF/ELSE -------------

if (turno == "V") or (turno == "v"):
    turno="Boa Tarde!"
elif (turno == "M") or (turno == "m"):
    turno="Bom dia!"
elif (turno == "N") or (turno == "n"):
    turno="Boa noite!"
else:
    turno="Turno invalido"
    nome=" "

print("------------------------------- \n")
print(turno +" "+ nome)