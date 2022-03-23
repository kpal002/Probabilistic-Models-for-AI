from factor import *
from functools import reduce
import copy

# describes a distribution over a cluster graph
# as parameterized by betas (factors over the clusters)
# and mus (factors over the sep-sets)
class clusterdist:
    # U is the clustergraph on which this distribution is based
    # alpha is a mapping from factors to cluster indexes in U
    def __init__(self,U,alpha):
        self._U = copy.copy(U) # so that the original can change
        self._beta = [] # list of local factors, _beta[i] matches cluster i in U
        self._mu = {} # dictionary mapping (i,j) to factor for edge i-j
                # note that (3,5) and (5,3) are the same, so we only
                # keep (3,5) -- because 3<5
        self._initializegraph(alpha)

    # assumes that sep-set is intersection of scopes of either side
    # (this is true for clique trees, but not necessarily true for other cluser graphs)
    def _initializegraph(self,alpha):
        for i in range(len(self._U.clusters)):
            self._beta.append(discretefactor(self._U.clusters[i],1.0))
        for i in range(len(self._U.clusters)):
            for j in self._U.adj(i):
                if i<j:
                    self._mu[(i,j)] = discretefactor(self._U.clusters[i] & self._U.clusters[j],1.0)
        for f,i in alpha.items():
            self._beta[i] = self._beta[i] * f

    @property
    def graph(self):
        return self._U

    # after calibration, should be the marginal over the cluster i
    def getbeta(self,i):
        return self._beta[i]

    # after calibration, should be the marginal over the sep-set btwn i&j
    def getmu(self,i,j):
        return self._mu[(i,j)] if i<j else self._mu[(j,i)]

    # calibrates, assuming that the clustergraph is a *forest*
    # (not necessarily a tree, despite the name -- it might be
    #  multiple disconnected trees -- this happens often once
    #  evidence is introduced)


    def setmu(self ,i,j,f):
        if i<j: 
            self._mu[(i,j)] = f
        else:
            self._mu[(j,i)] = f

    def bumsg(self,i,j):
        sigma = self._beta[i].marginalize(self._beta[i].scope - self.getmu(i,j).scope) 
        oldbeta = self._beta[j]
        self._beta[j] = self._beta[j]*sigma / self.getmu(i,j) 
        betadiff = (self._beta[ j] - oldbeta).maxabs()
        self.setmu(i ,j ,sigma)
    

    def treepassup(self ,cleft ,root):
        cleft.remove(root)
        for i in self._U.adj(root):
            if i in cleft: 
                self.treepassup(cleft ,i) 
                self.bumsg(i,root)


    def treepassdown( self , cleft , root ):
        cleft.remove(root)
        for i in self._U.adj(root):
            if i in cleft:
                self.bumsg(root,i) 
                self.treepassdown(cleft ,i)



    def treepass(self , cleft ):
        root = next(iter(cleft))
        self.treepassup (copy.copy(cleft) , root )
        self .treepassdown(cleft ,root)

    def forestpass(self ):
        cleft = set(range(len(self._U.clusters)))
        while len( cleft )>0: 
            self.treepass(cleft)


    def treecalibrate(self):
        ### For you to write (along with any helper methods you wish)
        self.forestpass()
