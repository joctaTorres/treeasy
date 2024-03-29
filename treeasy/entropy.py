from math import log2
from typing import List


def collection_entropy(collection: List[int]) -> float:
    """
        collection:     discrete target attribute count
                        e.g.1: [7, 9, 4]
    """

    collection_size = sum(collection)
    return entropy([(target / collection_size) for target in collection])


def entropy(probabilities: List[float], log=log2) -> float:
    """
        probabilities:  e.g.1: [(7/20), (9/20), (4/20)]
                        e.g.2: [(4/11), (7/11)]
                        e.g.3: [0.5, 0.2, 0.1, 0.1, 0.1]
    """

    if not probabilities:
        return 0

    entropy = 0

    for p in probabilities:
        term = p * log(p)
        entropy -= term

    return entropy


def target_collection_information_gain(
    target_collection: List[int], attribute_subsets: List[List[int]]
) -> float:
    target_instance_size = sum(target_collection)
    target_entropy = collection_entropy(target_collection)

    return attribute_information_gain(
        target_entropy, target_instance_size, attribute_subsets
    )


def attribute_information_gain(
    target_entropy: float, target_instance_size: int, attribute_subsets: List[List[int]]
) -> float:
    attribute_entropy = 0.0

    for subset in attribute_subsets:
        subset_weigth = sum(subset) / target_instance_size
        attribute_entropy += subset_weigth * collection_entropy(subset)

    gain = target_entropy - attribute_entropy
    return gain
