#!/usr/bin/env python2
# map_friends_rec.py
#MProcedimiento Map para recomendar amigos
import itertools
import sys
# La entrada proviene de un standard input
for linea in sys.stdin:
    # Se remueven los espacios en blanco
    linea = linea.strip()
    linea = linea.split("\t")
    k = int(linea[0])
    if len(linea) > 1:
        friends = linea[1]
        if friends != '':
            friends = linea[1].split(",")
            friends = sorted(map(int,friends))
            for ami in friends:
                par = tuple(sorted([k,ami]))
                par = ','.join(map(str,par))
                print par,"\t",1
            for par in itertools.combinations(friends,2):
                par = ','.join(map(str,par))
                print par,"\t",0