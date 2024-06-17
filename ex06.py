"""Faça o computador escolher um numero de 0 a 5 e tente advinhar 
Faça o computador aguardar 2 segundos antes de mostrar a resposta"""

from time import sleep
from random import randint
print("Vou escolher um numero de 1 a 5 tente advinhar")
aleatorio = randint(0,5)

numero = int(input("Informe o numero"))

print("><-" *10 )
print("PROSSESSANDO")
sleep(2)

if numero == aleatorio:
    print("Voce venceu, acertou eu pensei no numero {}".format(aleatorio))
else:
    print("Voce Perdeu eu pensei no numero {} e não {}".format(aleatorio,numero))