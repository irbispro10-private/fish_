import math

import numpy as np
import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()

def P_full(P0, _lambda, P_ob, P_lt, Z): # полная вероятность
    N = len(Z)
    restult = 0
    for j in range(N):
        tmp = P0[j]* P_i(P_ob, P_lt, Z, j)
        restult+=tmp
    return restult

def P_baies(P, P_ob, P_lt, Z, index):

    return P*P_i(P_ob, P_lt, Z, index)/P_full(Z, 0.5, P_ob, P_lt, Z)


def Pt(P0, N, _lambda, t): #априорная вероятность
    return (P0-1/N)*np.exp((-1*_lambda*N*t)/(N-1))+1/N

def P_i(P_ob, P_lt, Z, index): #условная вероятность
    tmp=np.power(P_ob, Z[index])*np.power((1-P_ob), (1-Z[index]))
    for i,z in enumerate(Z):
        if i != index:
            tmp*=np.power(P_lt, Z[i])*np.power((1-P_lt), (1-Z[i]))

    return tmp


period = 12
day = 2
P_ob=0.9
P_lt=0.05
P0 = 0.9

Z= [[1,0,0,0], [1,0,0,0], [0,0,1,0], [0,0,1,0], [1,0,0,0], [1,0,0,0]]
# Z= [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]
d = []
for i in range(period):
    if i%day==0:
        d.append(i)

print(d)

print(P_baies(Z[0][0], P_ob, P_lt, Z[0], 0))
print(P_baies(Z[0][1], P_ob, P_lt, Z[0], 1))
print(P_baies(Z[0][2], P_ob, P_lt, Z[0], 2))
print(P_baies(Z[0][3], P_ob, P_lt, Z[0], 3))


X = [[],[],[],[]]
Y = [[],[],[],[]]
P = (P_baies(Z[0][0], P_ob, P_lt, Z[0], 0))



for t in range(len(Z[0])):
    i = 0
    k = 0
    while i < period:
        X[t].append(i)

        if i in d:
            P = P_baies(Z[k][t], P_ob, P_lt, Z[t], t)
            j = 0
            k=k+1
        else:
            P = Pt(P, len(Z[0]), 0.5, j)

        Y[t].append(P)
        i=i+0.5
        j=j+0.5


print(Y)

plt.plot(X[0], Y[0])
plt.plot(X[1], Y[1], ":r")
plt.plot(X[2], Y[2], ":b")

plt.show()
