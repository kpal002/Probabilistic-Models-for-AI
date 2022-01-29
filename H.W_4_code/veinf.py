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
def veinf(fs,X,Y,elimorder=[]):

    # TO BE IMPLEMENTED BY YOU!

# same as above, but y is an assignment (not just a set of variables)
# and so the returned factor is just over X (the probabilty of X given Y=y)
# see veinf about elimorder!!
# reduce the factors before eliminating (otherwise, you will do too much
#  computational work)
def veinfval(fs,X,y,elimorder=[]):
    # in case this helps:
    # y is a dictionary (mapping from variables to values)
    # thus y.keys() is the set of variables

    # TO BE IMPLEMENTED BY YOU!
