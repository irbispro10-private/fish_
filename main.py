import numpy as np
def P_z_xi(Z, Po, Pl, index, k):
    p_z_xi = np.power(Po, Z[k][index])*np.power((1-Po), (1-Z[k][index]))
    for i in range(len(Z[k])):
        if i!=index:
            p_z_xi*=(np.power(Pl, Z[k][i])*np.power((1-Pl), (1-Z[k][i])))
    return p_z_xi

def Pt(P0, N, _lambda, t):
    return (P0-1/N)*np.exp((-1*_lambda*N*t)/(N-1))+1/N

def P_x_z(Z, index, P0, _lambda, t, Po, Pl, period):
    tmp = 0
    for i in len(Z[t/period]):
        tmp+=(Pt(P0, len(Z[0]), _lambda, t) * P_z_xi(Z, Po, Pl, index, t / period))
    res = (Pt(P0, len(Z[0]), _lambda, t)*P_z_xi(Z, Po, Pl, i, t/period))/tmp
    return res



Z = [[0,0,0,1],[0,1,0,0],[1,0,0,0]]

print(P_z_xi(Z, 0.9, 0.1, 0,1))