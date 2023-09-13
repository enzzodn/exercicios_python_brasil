#Q.4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

import os 
os.system('cls')

print("--------------------------------")
print("-------- MEDIA BIMESTRAL -------")
print("--------------------------------")

print("Digite suas 4 notas bimestrais e sera dita sua media e seu resultado final: \n")
n1=input("N1: ")
n2=input("N2: ")
n3=input("N3: ")
n4=input("N4: ")
print("---------------")

m=(float(n1)+float(n2)+float(n3)+float(n4))/4

print("Sua media foi: "+str(m))

"""if (m<=7):
    print("sua ")"""