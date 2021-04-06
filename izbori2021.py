from collections import namedtuple
from itertools import combinations

Partija = namedtuple('ПП', ['ime', 'mandati'])

prarlament = [
    Partija('ГЕРБ-СДС', 75),
    Partija('ИМА ТАКЪВ НАРОД', 51),
    Partija('БСП за БЪЛГАРИЯ', 43),
    Partija('ДВИЖЕНИЕ за ПРАВА и СВОБОДИ', 30),
    Partija('ДЕМОКРАТИЧНА БЪЛГАРИЯ', 27),
    Partija('ИЗПРАВИ СЕ! МУТРИ ВЪН!', 14)
]



vsicki_kombinacii = []


for nomer in range(0, len(prarlament) + 1):  
    for subset in combinations(prarlament, nomer):
        vsicki_kombinacii.append(subset)



for combinacija in vsicki_kombinacii:
    if combinacija:
        mandatinad120 = 0
        for partija in combinacija:
            mandatinad120 += partija.mandati
        if mandatinad120 >= 120:
            # За създаване на файл
            # with open('cominacii001.txt', 'a', encoding='utf-8') as f:
            #     for pari in combinacija:
            #         f.write(f'{pari.ime}, \t')
            #     f.write(f'\nобщо: {mandatinad120} \n\n')

            for pari in combinacija:
                print(f'{pari.ime}, \t', end='')
            print(f'\nобщо: {mandatinad120} \n')
