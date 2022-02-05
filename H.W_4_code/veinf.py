from functools import reduce
# implements VE inference
# Note: you should *not* change the passed in factorset, fs
# Make your own copy to work on if you need to.
# You will need to keep an index of which variables can be found
# in which factors in order to make the entire algorithm O(c*n*ln n)
#
# I would recommend writing a single "ve" function and calling it
# from veinf and veinfval

# should return a factor of the distribution of X given Y (X and Y are scopes)
# as calculated from the factorset fs
# returned value will be a factor over the union of X and Y
#
# NOTE!!!  elimorder may mention variables that are not to be eliminated!
#   elimorder may not mention variable that are to be eliminated!
# You should eliminate the variables that should be eliminated in the
#  order specified by elimorder (ignoring variables that should stay)
#  and, after all of those are done, eliminate variables not mentioned
#  in elimorder


def ve(factors,elimorder):
    
    phi = factors
    varriables = elimorder
    phi_dprime = set(phi)


    
    if elimorder == []:
        return set()
    
    # Loop over variables to be eliminated
    for var in elimorder:
        phi_prime = set()
        
        #print(var)
        for fac in phi:
            scope = fac.vars

            if var in scope:
                
                phi_prime = phi_prime.union({fac})
                
                phi_dprime = phi_dprime - phi_prime
    
                    
        psi = reduce((lambda x, y: x * y), phi_prime)

        tau = psi.marginalize({var})
        #print(tau)
        phi_dprime = phi_dprime.union({tau})
        phi = phi_dprime

    
    return phi_dprime.union({tau})

def veinf(fs,X,Y,elimorder=[]):

    # TO BE IMPLEMENTED BY YOU!

    # same as above, but y is an assignment (not just a set of variables)
    # and so the returned factor is just over X (the probabilty of X given Y=y)
    # see veinf about elimorder!!
    # reduce the factors before eliminating (otherwise, you will do too much
    #  computational work)
    elimorder = sorted(set(elimorder), key=elimorder.index)

    ini_eli = [item for item in elimorder if item not in list(X.union(Y))]
    final_eli = [item for item in list(fs.vars) if ((item not in ini_eli) and (item not in list(X.union(Y))))]
    
    phi = ve(fs.factors,ini_eli)
    if len(ini_eli) == 0:
        phi_star = ve(fs.factors,final_eli)
    elif len(final_eli) == 0:
        phi_star = phi
    else:
        phi_star = ve(list(phi),final_eli)

    phi_star_new = reduce((lambda x, y: x * y), phi_star)
    phi_star_new = phi_star_new/phi_star_new.marginalize(X)
    return phi_star_new

def veinfval(fs,X,y,elimorder=[]):

    return veinf(fs,X,y.keys(),elimorder=[]).reduce(y)


