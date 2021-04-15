# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:25:38 2021

@author: kmajk
"""

import numpy as np
def generGeo(x_0, x_p, n):
    tab = (x_p - x_0) / (n - 1)
    macierz = np.array([x_0])
    i = []
    for i in range(1, n, 1):
        macierz = np.block([macierz, i * tab + x_0])
    return i, macierz