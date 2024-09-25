# Crie um programa que faça uma contagem regressiva de 10 até 0 e exiba "FIM!" ao final.
from time import sleep


for uff in range (10, -1, -1):
    print(uff)
    sleep(1)
print ("FIM!")