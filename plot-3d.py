#!/usr/bin/python
# -*- coding: utf-8 -*-
#===================================#
# File name: 						#
# Author: Vitor dos Santos Batista	#
# Date created: 					#
# Date last modified: 				#
# Python Version: 2.7				#
#===================================#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

n = 194
d = np.load('pop-%i.npy' %(n))
x1 = d[0]
y1 = d[1]
z1 = np.load('fit-%i.npy' %(n))

#Avaliação
def f6(x, y):
    #x = [decodifica(i, _min, _max, _bits, _preci) for i in pop[:,:22]]
    #y = [decodifica(i, _min, _max, _bits, _preci) for i in pop[:,22:]]
    sq = x**2+y**2
    num = np.sin(np.sqrt(sq))**2 -0.5
    den = (1.+0.001*(sq))**2
    return 0.5 + num/(den*den)

k = 100
x = np.arange(-k, k, 0.1)
y = np.arange(-k, k, 0.1)
X, Y = np.meshgrid(x, y)
z = f6(X, Y)
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X, Y, z, cmap=cm.coolwarm,
                    linewidth=0.1)

ax.plot(x1, y1, z1, 'o')
ax.set_title('G%i' %(n))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f6')

plt.show()
