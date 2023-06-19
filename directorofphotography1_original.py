# 
def get_indices(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def is_between(p, a, b):
    return (p < a & a < b) | (b < a & a < p)

def in_interval(a, p, X, Y):
    return X <= abs(a - p) & abs(a - p) <= Y

def is_legitimate(p, a, b, X, Y):
    return in_interval(a, p, X, Y) & in_interval(b, a, X, Y) & is_between(p, a, b)

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    pindex = get_indices(C, 'P')
    andex = get_indices(C, 'A')
    bindex = get_indices(C, 'B')
    print(pindex,' ',andex,' ',bindex)
    
    nbr = 0
    for p in pindex:
        for a in andex:
            for b in bindex:
                if is_legitimate(p, a, b, X, Y):
                    nbr = nbr + 1
    return nbr
                
