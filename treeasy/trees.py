import pandas as pd

from treeasy.entropy import attribute_information_gain, collection_entropy
from treeasy.types import Tree


def tree_id3(examples, target_attribute, attributes):
    """
        @params:
        examples: are the training examples.
        target_attribute: is the attribute whose value is to be predicted by the tree.
        attributes: is a list of other attributes that may be tested by the learned decision tree.
        @returns: a decision tree that correctly classifies the given examples
    """
    # if all attribute have been tested.. return most common target
    if len(attributes) == 0:
        target_attribute_mode = get_column_values_count(
            examples[target_attribute]
        ).idxmax()
        return Tree(target_attribute_mode)

    # get counts of target attributes. e.g.: [9, 5]
    target_attribute_values = list(get_column_values_count(examples[target_attribute]))

    # collection S entropy:
    target_attribute_entropy = collection_entropy(target_attribute_values)

    if target_attribute in attributes:
        attributes.remove(target_attribute)

    # if theres only one attribute create a leaf node
    if len(target_attribute_values) == 1:
        return Tree(get_column_values_count(examples[target_attribute]).idxmax())

    # get total of instances
    target_instance_size = sum(target_attribute_values)

    # find the attribute with the highest information gain
    max_information_gain_attribute = get_max_information_gain_attribute(
        examples,
        attributes,
        target_attribute,
        target_attribute_entropy,
        target_instance_size,
    )

    # create a node for it
    root = Tree(max_information_gain_attribute)

    #  for each possible value of the attribute (max gain attribute), run the algorithm for its subset
    children_branches = []
    for value in examples[max_information_gain_attribute].unique():
        examples_subset = get_attribute_value_dataframe(
            examples, max_information_gain_attribute, value
        )

        if max_information_gain_attribute in attributes:
            attributes.remove(max_information_gain_attribute)
        children_branches.append(
            (value, tree_id3(examples_subset, target_attribute, attributes))
        )

    root.set_children(children_branches)
    return root


def get_max_information_gain_attribute(
    examples,
    attributes,
    target_attribute,
    target_attribute_entropy,
    target_instance_size,
):
    attribute_gains = get_attribute_gains(
        examples,
        attributes,
        target_attribute,
        target_attribute_entropy,
        target_instance_size,
    )
    return max(attribute_gains, key=attribute_gains.get)


def get_attribute_gains(
    examples,
    attributes,
    target_attribute,
    target_attribute_entropy,
    target_instance_size,
):
    attribute_gains = {}
    for attribute in attributes:
        attribute_subset_values = get_attribute_subset_values(
            examples, attribute, target_attribute
        )
        information_gain = attribute_information_gain(
            target_attribute_entropy, target_instance_size, attribute_subset_values
        )

        attribute_gains.update({attribute: information_gain})

    return attribute_gains


def get_attribute_subset_values(examples, attribute, target_attribute):
    attribute_values_subset = []
    for value in examples[attribute].unique():
        value_subset_df = get_attribute_value_dataframe(examples, attribute, value)
        attribute_values_subset.append(
            get_column_values_count(value_subset_df[target_attribute])
        )

    return attribute_values_subset


def get_attribute_value_dataframe(original_df, column, value):
    return original_df.loc[original_df[column] == value]


def get_column_values_count(column):
    return column.value_counts()


def test_tree_id3_tennis():
    training_data = pd.read_csv("./datasets/tennis.csv")
    training_data.drop(["day"], axis=1, inplace=True)

    attributes = list(training_data.columns)
    target = "play"

    t = tree_id3(training_data, target, attributes)
    with open("result_play_tennis.json", "w") as result:
        result.write(str(t))


def test_tree_id3_cars():
    training_data = pd.read_csv("./datasets/cars.csv")
    training_data.drop(["car"], axis=1, inplace=True)

    attributes = list(training_data.columns)
    target = "buying"

    t = tree_id3(training_data, target, attributes)
    with open("result_cars.json", "w") as result:
        result.write(str(t))


def test_tree_id3_iris():
    training_data = pd.read_csv("./datasets/iris.csv")

    attributes = list(training_data.columns)
    target = "variety"

    t = tree_id3(training_data, target, attributes)
    with open("result_iris.json", "w") as result:
        result.write(str(t))


if __name__ == "__main__":
    test_tree_id3_tennis()
