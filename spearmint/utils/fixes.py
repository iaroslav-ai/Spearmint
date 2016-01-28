import sys

def items(x):
    if sys.version < '3':
        return x.iteritems()
    return x.items()

def xrange(x):
    if sys.version < '3':
        return xrange(x)
    return range(x)
