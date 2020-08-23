# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:31:24 2020

@author: ASUS
"""
import  matplotlib.pyplot as plt
import  numpy as np

# gradient descent

# 從 (4,4) 找到 
# y = x1^2 +x2^2 最低點

def f(x1,x2):
    return x1**2 + x2**2


def defferental(f,x1,x2):
    '''
    二階篇微分
    '''
    h = 1e-4
    a = (f(x1+h,x2) - f(x1,x2)) /h
    b = (f(x1,x2+h) - f(x1,x2)) /h
    return np.array([a,b])


# defferental(f,3.0,4.0)
# defferental(f,0.0,2.0)# 爆掉了
# defferental(f,3.0,0.0)


def defferental2(f,x1,x2):
    '''
    二階篇微分
    數值分析法
    '''
    h = 1e-4
    a = (f(x1+h,x2) - f(x1-h,x2)) /(2*h)
    b = (f(x1,x2+h) - f(x1,x2-h)) /(2*h)
    return np.array([a,b])

defferental2(f,3.0,4.0)
defferental2(f,0.0,2.0)# 正常了
defferental2(f,3.0,0.0)


lr = 0.2
tel = 1E-10
point = defferental2(f,-3.0,4.0)

x=[-3.0]
y=[4.0]

'''
gradient descent
'''
while  abs(point[0])> tel and abs(point[1])>tel:
    point = point - lr * defferental2(f, point[0], point[1])
    x.append(point[0])
    y.append(point[1])


'''
繪圖
'''

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

# ax.plot( [-5, 5], [0,0], '--b') 
# ax.plot( [0,0], [-5, 5], '--b')
ax.plot(x,y,'o')


# 計算等高線
delta = 0.25
tx = np.arange(-6.0, 6.0, delta)
ty = np.arange(-6.0, 6.0, delta)
X, Y = np.meshgrid(tx, ty)
Z = f(X, Y)
CS = ax.contour(X, Y, Z, levels=15)
ax.clabel(CS, inline=1, fontsize=10)



