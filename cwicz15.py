import numpy as np

def fun2(x):
    tab2=[]
    for i in x:
        if i<0:
            tab2.append(np.sin(i))
        else:
            tab2.append(np.sqrt(i))
    return tab2
