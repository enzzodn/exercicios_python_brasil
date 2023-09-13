#Q.4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

import os 


os.system('cls')

char=input("Digite uma letra e veremos se eh uma vogal ou uma consoante: ")

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or \
        char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
    print("Sua letra eh uma vogal")
else:
    print("Eh uma consoante")
    