from typing import List
from math import log2

def collection_entropy(collection : List[int]) -> float:
    '''
        collection:     discrete target attribute count
                        e.g.1: [7, 9, 4]
    '''

    collection_size = sum(collection)
    return entropy([(target/collection_size) for target in collection])


def entropy(probabilities : List[float], log=log2) -> float:
    '''
        probabilities:  e.g.1: [(7/20), (9/20), (4/20)]
                        e.g.2: [(4/11), (7/11)]
                        e.g.3: [0.5, 0.2, 0.1, 0.1, 0.1]
    '''

    if not probabilities:
        return 0

    entropy = 0

    for p in probabilities:
        term = (p*log(p))
        entropy -= term
    
    return entropy



