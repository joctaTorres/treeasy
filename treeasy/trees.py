from anytree import Node, RenderTree
import pandas as pd

from entropy import attribute_information_gain, collection_entropy


def treeID3(
    examples,
    target_attribute,
    attributes,
    target_attribute_values=None,
    target_attribute_mode=None,
    target_instance_size=None,
    target_attribute_entropy=None,
):
    """
        @params:
        examples: are the training examples.
        target_attribute: is the attribute whose value is to be predicted by the tree.
        attributes: is a list of other attributes that may be tested by the learned decision tree.
        
        @returns: a decision tree that correctly classifies the given examples
    """
    
    if not target_attribute_values:
        target_attribute_values = list(
            get_column_values_count(examples[target_attribute])
        )

    if not target_attribute_mode:
        target_attribute_mode = get_column_values_count(examples[target_attribute]).idxmax()

    if examples.empty:
        return Node(target_attribute_mode)

    if not target_instance_size:
        target_instance_size = sum(target_attribute_values)

    if not target_attribute_entropy:
        target_attribute_entropy = collection_entropy(target_attribute_values)

    if target_attribute in attributes:
        attributes.remove(target_attribute)

    if len(target_attribute_values) == 1:
        return Node(
            get_column_values_count(examples[target_attribute]).idxmax()
        )

    max_information_gain_attribute = get_max_information_gain_attribute(
        examples,
        attributes,
        target_attribute,
        target_attribute_entropy,
        target_instance_size,
    )

    # import pdb; pdb.set_trace()
    root = Node(max_information_gain_attribute)

    children_branches = []
    for value in examples[max_information_gain_attribute].unique():
        examples_subset = get_attribute_value_dataframe(examples, max_information_gain_attribute, value)
        children_branches.append(
            treeID3(
                examples_subset,
                target_attribute,
                attributes,
                # target_attribute_values=target_attribute_values,
                # target_instance_size=target_instance_size,
                # target_attribute_entropy=target_attribute_entropy,
                # target_attribute_mode=target_attribute_mode,
            )
        )

    root.children = children_branches
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


def test_treeID3():
    training_data = pd.read_csv("./datasets/tennis.csv")
    training_data.drop(["day"], axis=1, inplace=True)

    attributes = list(training_data.columns)
    target = "play"

    t = treeID3(training_data, target, attributes)
    print(RenderTree(t))


if __name__ == "__main__":
    test_treeID3()
