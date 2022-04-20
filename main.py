import math

import numpy as np
import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()

def P_full(P0, _lambda, t, P_ob, P_lt, Z): # полная вероятность
    N = len(Z)
    restult = 0
    for j,z in enumerate(Z):
        restult+=Pt(P0, N, _lambda, t)* P_i(P_ob, P_lt, Z, j)
    return restult

def P_baies(P, P_ob, P_lt, Z, index):
    N = len(Z)
    restult = 0
    for j, z in enumerate(Z):
        restult += P[j] * P_i(P_ob, P_lt, Z, j)

    restult = (P[index]*P_i(P_ob, P_lt, Z, index))/restult
    return restult

def Pt(P0, N, _lambda, t): #априорная вероятность
    return (P0-1/N)*np.exp((-1*_lambda*N*t)/(N-1))+1/N

def P_i(P_ob, P_lt, Z, index): #условная вероятность
    tmp=np.power(P_ob, Z[index])*np.power((1-P_ob), (1-Z[index]))
    for i,z in enumerate(Z):
        if i != index:
            tmp*=np.power(P_lt, Z[i])*np.power((1-P_lt), (1-Z[i]))

    return tmp


period = 2
P_ob=0.9
P_lt=0.05



Z = [[0,1,0,0],[0,1,1,0],[1,0,0,0],[0,0,1,0],[1,0,0,0],[1,0,1,0],[1,0,0,0]]



X = []
Y = []
for i in range(len(Z[0])):
    X.append([])
    Y.append([])
    Y[i].append(P_baies(Z[0], P_ob, P_lt, Z[math.floor(0/period)], i))

print(X,Y)

for index, x in enumerate(range(0,14)):
    for i in range(len(Z[0])):
        X[i].append(x)
        tmp = []
        for j in range(len(Z[0])):
            tmp.append(Y[j][index])
        Y[i].append(Pt(P_baies(tmp, P_ob, P_lt, Z[math.floor(index/period)], 1), 4, 0.5, x))

print(Y)
print(X)
plt.plot(X[1][:14], Y[1][:14], ':b')

# plt.plot(x, P_i(P_ob, P_lt, Z[np.round(float(x/period))], 0))
# plt.plot(x, Pt(0.9, 5, 0.5, x), ':b')
plt.show()
# print(P_z_xi(Z, 0.9, 0.1, 0,1))