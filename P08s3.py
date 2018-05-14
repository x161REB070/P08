# Programmu veidoja: Karlis Reinis Ulmanis */
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

v = 70+8
g = 9.81
t = 0
for i in range(0,100,1):
    t = 1 / (float(i) + 1)
    y = (v * t)-((g * t ** 2) / 2)
    print 'Pec %.3f sekundem bumba bus %.2f metru augstuma \n' %(t,y)
