from factor import *
from factorset import *
from veinf import *
from itertools import product

# while this code does one test of your VE algorithm,
# it is not complete and your algorithm will be tested on
# different examples

def makefactor(vars,vals):
    phi = discretefactor(set(vars))
    for j,x in enumerate(product(*map((lambda v : [(v,i) for i in range(v.nvals)]),vars))):
        s = {a:b for (a,b) in x}
        phi[s] = vals[j]
    return phi

def buildnewstudentex():
    c = discretevariable("c",2)
    d = discretevariable("d",2)
    t = discretevariable("t",2)
    i = discretevariable("i",2)
    g = discretevariable("g",3)
    s = discretevariable("s",2)
    l = discretevariable("l",2)
    j = discretevariable("j",2)

    studentbn = factorset()

    studentbn.addfactor(makefactor([c],[0.5,0.5]))
    studentbn.addfactor(makefactor([c,d],[0.4,0.6,0.8,0.2]))
    studentbn.addfactor(makefactor([i],[0.6,0.4]))
    studentbn.addfactor(makefactor([i,t],[0.9,0.1,0.4,0.6]))
    studentbn.addfactor(makefactor([t,d,g],
        [0.3,0.4,0.3,
         0.05,0.25,0.7,
         0.9,0.08,0.02,
         0.5,0.3,0.2]))
    studentbn.addfactor(makefactor([t,s],[0.95,0.05,0.2,0.8]))
    studentbn.addfactor(makefactor([g,l],[0.1,0.9,0.4,0.6,0.99,0.01]))
    studentbn.addfactor(makefactor([l,s,j],
        [0.9,0.1,
            0.4,0.6,
            0.3,0.7,
            0.1,0.9]))

    return studentbn,(c,d,t,i,g,s,l,j)


if __name__ == '__main__':
    studentex,(c,d,t,i,g,s,l,j) = buildnewstudentex()
    # all of these should be the same result (different running times)
    print(veinf(studentex,{j},set()))
    print(veinf(studentex,{j},set(),[c,d,s,j,l]))
    print(veinf(studentex,{j},set(),[g,c,s,d,l]))
    # same for these:
    print(veinf(studentex,{i,j},set()))
    print(veinf(studentex,{i,j},set(),[l,j,l,s,g]))
    print(veinf(studentex,{i,j},set(),[c,d,t,i,g,s,l,j]))
    # same for these:
    print(veinf(studentex,{c,i},{g,j}))
    print(veinf(studentex,{c,i},{g,j},[d,c,i,t,g,s]))
    # same for these:
    print(veinfval(studentex,{c,i},{g:1}))
    print(veinfval(studentex,{c,i},{g:1},[s,g,t,i,c,d]))
