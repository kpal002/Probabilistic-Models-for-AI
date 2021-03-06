# construct with factorset()
# can only add (not remove) factors, currently
# use fs.vars to get the set of variables mentioned in the factors
# use fs.factors to get an array of the factors

class factorset:
    def __init__(self):
        self._factors = []
        self._vars = set()

    def addfactor(self,f):
        i = len(self._factors)
        self._factors.append(f)
        for v in f.vars:  # doing set union takes longer b/c must make new set!
            self._vars.add(v)

    @property
    def vars(self):
        return self._vars

    @property
    def factors(self):
        return self._factors
