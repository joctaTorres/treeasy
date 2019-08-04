import pandas as pd

from entropy import attribute_information_gain, collection_entropy


def treeID3(examples, target_attribute, attributes):
    """
        @params:
        examples: are the training examples.
        target_attribute: is the attribute whose value is to be predicted by the tree.
        attributes: is a list of other attributes that may be tested by the learned decision tree.
        
        @returns: a decision tree that correctly classifies the given examples
    """

    target_attribute_values = get_column_values(examples[target_attribute])
    target_instance_size = sum(target_attribute_values)
    target_attribute_entropy = collection_entropy(target_attribute_values)

    for attribute in attributes:
        attribute_subset_values = get_attribute_subset_values(
            examples, attribute, target_attribute
        )
        information_gain = attribute_information_gain(
            target_attribute_entropy, target_instance_size, attribute_subset_values
        )


def get_attribute_subset_values(examples, attribute, target_attribute):
    attribute_values_subset = []
    for value in examples[attribute].unique():
        value_subset_df = get_attribute_value_dataframe(examples, attribute, value)
        attribute_values_subset.append(
            get_column_values(value_subset_df[target_attribute])
        )

    return attribute_values_subset


def get_attribute_value_dataframe(original_df, column, value):
    return original_df.loc[original_df[column] == value]


def get_column_values(column):
    return list(column.value_counts()) or 0


def test_treeID3():
    training_data = pd.read_csv("./datasets/tennis.csv")
    training_data.drop(["day"], axis=1, inplace=True)

    attributes = list(training_data.columns)
    target = "play"

    treeID3(training_data, target, attributes)

    import pdb

    pdb.set_trace()


if __name__ == "__main__":
    test_treeID3()
