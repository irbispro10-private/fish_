import math

import numpy as np
import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()
def P_z_xi(Z, Po, Pl, index, k):
    p_z_xi = np.power(Po, Z[k][index])*np.power((1-Po), (1-Z[k][index]))
    for i in range(len(Z[k])):
        if i!=index:
            p_z_xi*=(np.power(Pl, Z[k][i])*np.power((1-Pl), (1-Z[k][i])))
    return p_z_xi

def Pt(P0, N, _lambda, t): #априорная вероятность
    return (P0-1/N)*np.exp((-1*_lambda*N*t)/(N-1))+1/N

def P_i(P_ob, P_lt, Z, index): #условная вероятность
    tmp=np.power(P_ob, Z[index])*np.power((1-P_ob), (1-Z[index]))
    print(tmp)
    for i,z in enumerate(Z):
        if i != index:
            tmp*=np.power(P_lt, Z[i])*np.power((1-P_lt), (1-Z[i]))
    print(tmp)


period = 20
P_ob=0.9
P_lt=0.05



Z = [[0,1,0,0],[0,1,0,0],[1,0,0,0]]

P_i(P_ob, P_lt, Z[0], 0)

X = []
Y = []

for x in range(0,60):
    X.append(x)
    Y.append(P_i(P_ob, P_lt, Z[math.floor(x/period)], 0))
plt.plot(np.array(X), np.array(Y), ':b')
# plt.plot(x, P_i(P_ob, P_lt, Z[np.round(float(x/period))], 0))
# plt.plot(x, Pt(0.9, 5, 0.5, x), ':b')
plt.show()
print(P_z_xi(Z, 0.9, 0.1, 0,1))