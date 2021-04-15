# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:53:06 2021

@author: kmajk
"""
import numpy as np
import matplotlib.pyplot as plt
import funGenerGeo as fun
import rysuj as rys
# funkcja
c=0;
f=0;

twb_L = "D"
twb_P = "D"
wwb_L = 0
wwb_P = 1





wezly = np.array([[1,0],[2,1], [3,0.5], [4,0.75]])
elementy = np.array([[1, 3], [4, 2], [3, 4]])


rys.rys_geometria(wezly,elementy)
