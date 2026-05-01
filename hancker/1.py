#!/bin/python3

import math
import os
import random
import re
import sys


def funcao(n):
    if n % 2 != 0:
        print(f" {n} é impar") # Todos números impares
    elif (n % 2 == 0) and (2 <= n <= 5):
        print(f" {n} é Par e está entre 2 e 5") # 2 e 4 par
    elif (n % 2 == 0) and (6 <= n <= 20):
        print(f"{n} é par e está entre 6 e 20")
    elif (n % 2 == 0) and (n > 20):
        print(f"{n} é par e é maior do que 20")


funcao(22)
funcao(24)
funcao(25)
