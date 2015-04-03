# version code 3ebd92e7eece+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent
from vec import Vec

## 1: (Task 1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([ randGF2() for i in range(6)])
        if a0*u == s and b0*u == t:
            return u


## 2: (Task 2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
#'''
L=[Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: one, 4: one, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: one, 4: 0, 5: one}), Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: one, 4: 0, 5: one}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: one, 4: 0, 5: one}), Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: one, 4: one, 5: one}), Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: one, 4: one, 5: one}), Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: one, 5: one}), Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: one, 5: 0})]

secret_a0 =list2vec([one, one,   0, one,   0, one])
secret_b0 =list2vec([one, one,   0,   0,   0, one])
secret_a1 =L[0]
secret_b1 =L[1]
secret_a2 =L[2]
secret_b2 =L[3]
secret_a3 =L[4]
secret_b3 =L[5]
secret_a4 =L[6]
secret_b4 =L[7]

#print(choose_secret_vector(s,t))
#u = list2vec([ randGF2() for i in range(6)])
#print(u)

# Program for task 2
'''
L=list(range(0,8))
for n in range(100):
    u = [list2vec([ randGF2() for i in range(6)]) for j in range(8)]
    for k in range(28):
        S=list()
        random.shuffle(L)
        for i in range(3):
            S.append(u[L[i]])
        print("len S")
        print(k, len(u),len(S))
        if is_independent(S)==False:
            break
    if is_independent(S)==True:
        print(u)
'''
