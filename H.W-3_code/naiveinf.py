from functools import reduce
import operator

# implements naive inference
# by just forming the joint, then marginalizing out
# and then conditioning

# should return a factor of the distribution of X given Y (X and Y are scopes)
# as calculated from the factorset fs
# returned value will be a factor over the union of X and Y



def naiveinf(fs,X,Y):

    unnorm = reduce((lambda x, y: x * y), fs.factors)
    norm = unnorm.marginalize(unnorm.vars - X - Y)

    return norm/norm.marginalize(X)

    return norm
# same as above, but y is an assignment (not just a set of variables)
# and so the returned factor is just over X (the probabilty of X given Y=y)
def naiveinfval(fs,X,y):
    # in case this helps:
    # y is a dictionary (mapping from variables to values)
    # thus y.keys() is the set of variables
    
    return naiveinf(fs,X,y.keys( )).reduce(y)
    