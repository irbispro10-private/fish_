import math,csv
from sys import argv
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()

def find_index(arr, val):
    for i in arr:
        if i[0]==val:
            return [1, i]
    return [-1]
def csv_to_Z():
    z = []
    with open(argv[1], 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            tmp = []
            for i in row:
                tmp.append(int(i))
            z.append(tmp)
    return z

def csv_to_dynamic():
    Dyn = []
    P_lt = 0
    _lambda=0
    with open(argv[2], 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        Dyn = []
        i=True
        for row in spamreader:
            if i:
                _lambda = float(row[0].replace(',', '.'))
                P_lt = float(row[1].replace(',', '.'))
                i = False
            else:
                Dyn.append([float(row[0].replace(',', '.')),float(row[1].replace(',', '.'))])
                # print(float(row[1].replace(',', '.')))
    return [P_lt, _lambda, Dyn]

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
    return (P0-1/N)*math.exp((-1*_lambda*N*t)/(N-1))+1/N

def P_i(P_ob, P_lt, Z, index): #условная вероятность
    tmp=math.pow(P_ob, Z[index])*math.pow((1-P_ob), (1-Z[index]))
    for i,z in enumerate(Z):
        if i != index:
            tmp*=math.pow(P_lt, Z[i])*math.pow((1-P_lt), (1-Z[i]))

    return tmp

def write_res(X, Y, name):
    with open('dynamic/'+name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(X)):
            spamwriter.writerow([X[i],Y[i]])



period = int(argv[3])
day = 5
P_ob=0.9
P_lt=0
P0 = 0.9
step = 0.25

dynamic = csv_to_dynamic()
P_lt = dynamic[0]
_lambda = dynamic[1]

Z =csv_to_Z()
# Z= [[1,0,0,0], [1,0,0,0], [1,0,1,0], [0,0,1,0], [1,0,0,0], [1,0,0,0]]
# Z= [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]
d = []

for i in range(period):
    if i%day==0:
        d.append(i)

dyanmic = []

# print(P_baies(Z[0][0], P_ob, P_lt, Z[0], 0))
# print(P_baies(Z[0][1], P_ob, P_lt, Z[0], 1))
# print(P_baies(Z[0][2], P_ob, P_lt, Z[0], 2))
# print(P_baies(Z[0][3], P_ob, P_lt, Z[0], 3))


X = [[],[],[],[]]
Y = [[],[],[],[]]
P = (P_baies(Z[0][0], P_ob, P_lt, Z[0], 0))




for t in range(len(Z[0])):
    i = 0
    k = 0
    while i < period:
        X[t].append(i)
        time_index = find_index(dynamic[2], i)
        print(time_index)
        if time_index[0] != -1:
            print("a")
            P = P_baies(Z[k][t]*time_index[1][1], time_index[1][1], P_lt, Z[t], t)
            j = 0
            k=k+1
        else:
            P = Pt(P, len(Z[0]), _lambda, j)

        Y[t].append(P)
        i=i+step
        j=j+step



# plt.plot(X[0], Y[0])
# plt.plot(X[1], Y[1], "r")
# plt.plot(X[2], Y[2], ":g")
# plt.plot(X[3], Y[3], ":y")
#
# plt.show()
print(X[0])
for i in range(len(X)):
    write_res(X[i], Y[i], str(i)+'.csv')