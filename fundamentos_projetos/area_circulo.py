# -*- coding/. utf-8 -*-
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""\
            É necessário informar o raio do círculo.
            Sintaxe: area_circulo <raio>""")
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo: ', area)
