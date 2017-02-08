#!/usr/bin/env python2
#Método Reduce para recomendar amigos.
import itertools
import sys
recs = 10
def agregarPar(users,k1,k2,flag):
    if flag==1:
        flag = True
    else:
        flag = False
    if k1 not in users:
        users[k1] = {}
        users[k1][k2] = [1,False]
    else:
        if k2 in users[k1]:
            users[k1][k2][0] += 1
        else:
            users[k1][k2] = [1,False]
    if flag==True:
        users[k1][k2][0] -= 1
        users[k1][k2][1] = True

# Entrada proviene de un standard input.
users = {}

for linea in sys.stdin:
    linea = linea.strip()
    linea = linea.split("\t")
    key = tuple(map(int,linea[0].strip().split(",")))
    flag = int(linea[1])
    k1,k2 = key
    agregarPar(users,k1,k2,flag)
    agregarPar(users,k2,k1,flag)
for k1 in users.keys():
    recommend = []
    for k2 in users[k1].keys():
        n,nflag = users[k1][k2]
        if nflag==False:
            recommend.append((k2,n))
    recommend = sorted(recommend,key=lambda x: x[0])
    recommend = sorted(recommend,key=lambda x: x[1],reverse=True)
    if len(recommend)>0:
        recommend = list(map(str,zip(*recommend)[0]))
        print k1,"\t",','.join(recommend[:recs])