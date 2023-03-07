from random import randint
from time import sleep
from operator import itemgetter

ordem = {}
valores = {
    'V1': randint(1, 9),
    'V2': randint(1, 9),
    'V3': randint(1, 9),
    'V4': randint(1, 9),
}

for posicao, valor in valores.items():
    print(valor, end='')
    sleep(1)

ordem = sorted(valores.items(), key=itemgetter(1))

for i in range(4):
    print(ordem[i][1])
