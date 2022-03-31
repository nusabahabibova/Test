# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:22:00 2021

@author: Nushaba
"""
"""
l1 = [12,33,45,1]
l2 = [44,,500,3]

bu formada yazin [(12,44), (33, 500), (45,3)]

"""
#qısa olan listin uzunlughu qeder gedir deye qisa uzunluqda olanin uzunlughunu
#tapin
def minimum(a, b):
    if  a < b:
        return a
    return b

l1 = [12,33,45,1]
l2 = [44,500,3]
nl = []

for i in range(minimum(len(l1),len(l2))):
    nl.append((l1[i], l2[i]))
    
print(nl)

##########################

#siyahida tekrarlanan ededi tap

def maksimum(l):
    maks= l[0]
    for i in l:
        if maks< i:
            maks = i
    return maks

siyahi = [1, 4,2,5,7,7,4,1]

d = {}

for i in siyahi:
    d[i]= siyahi.count(i)
    
print(d)

maks = maksimum(list(d.values()))

print([key for key in d.keys() if d[key]==maks])
    
    