from math import log2

def entropy(probabilities, log=log2):
    '''
        probabilities: e.g [(7/20), (9/20), (4/20)] 
    '''

    if not probabilities:
        return 1.0

    entropy = 0

    for p in probabilities:
        term = (p*log(p))
        entropy -= term
    
    return entropy



