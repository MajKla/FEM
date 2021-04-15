# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:29:14 2021

@author: kmajk
"""
import numpy as np
import matplotlib.pyplot as plt

def rys_geometria(wezly, elementy):
    l_wezly = len(wezly)
    y = np.zeros(l_wezly)
    plt.plot(wezly[:,1],y,'r.')
    plt.show()