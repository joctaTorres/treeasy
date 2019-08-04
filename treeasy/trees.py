import pandas as pd
from anytree import Node

from entropy import collection_entropy


def treeID3(examples, target_attribute, attributes):
    '''
        @params:
        examples: are the training examples.
        target_attribute: is the attribute whose value is to be predicted by the tree.
        attributes: is a list of other attributes that may be tested by the learned decision tree.
        
        @returns: a decision tree that correctly classifies the given examples
    '''

    target_attribute_values = list(examples[target_attribute].value_counts())
    target_attribute_entropy = collection_entropy(target_attribute_values)

    import pdb; pdb.set_trace()


def test_treeID3():
    training_data = pd.read_csv("./datasets/tennis.csv")
    training_data.drop(['day'], axis=1, inplace=True)

    attributes = list(training_data.columns)
    target = "play"

    treeID3(training_data, target, attributes)


    import pdb; pdb.set_trace()


if __name__ == "__main__":
    test_treeID3()