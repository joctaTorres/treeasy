from unittest.mock import call, patch

from treeasy.entropy import (
    attribute_information_gain,
    collection_entropy,
    entropy,
    target_collection_information_gain,
)


def test_entropy(snapshot):
    snapshot.assert_match(entropy([(9 / 14), (5 / 14)]))
    snapshot.assert_match(entropy([0.5, 0.2, 0.1, 0.1, 0.1]))


def test_collection_entropy(snapshot):
    collection_entropy_one = collection_entropy([9, 5])
    collection_entropy_two = collection_entropy([7, 9, 4])

    entropy_one = entropy([(9 / 14), (5 / 14)])
    entropy_two = entropy([(7 / 20), (9 / 20), (4 / 20)])

    assert collection_entropy_one == entropy_one
    assert collection_entropy_two == entropy_two

    snapshot.assert_match(collection_entropy_one)
    snapshot.assert_match(collection_entropy_two)


@patch("treeasy.entropy.entropy")
def test_collection_entropy_call(entropy, snapshot):
    collection_entropy([9, 5])
    collection_entropy([7, 9, 4])

    entropy.assert_has_calls(
        [call([(9 / 14), (5 / 14)]), call([(7 / 20), (9 / 20), (4 / 20)])]
    )


def test_attribute_information_gain(snapshot):
    snapshot.assert_match(attribute_information_gain(0.940, 14, [[6, 2], [3, 3]]))
    snapshot.assert_match(attribute_information_gain(0.940, 14, [[3, 4], [6, 1]]))


@patch("treeasy.entropy.attribute_information_gain")
def test_target_collection_information_gain_call(attribute_information_gain):
    attribute_subsets = [[6, 2], [3, 3]]

    target_collection_information_gain([9, 5], attribute_subsets)

    attribute_information_gain.assert_called_once_with(
        0.9402859586706309, 14, attribute_subsets
    )


def test_target_collection_information_gain(snapshot):
    attribute_subsets = [[6, 2], [3, 3]]

    collection_result = target_collection_information_gain([9, 5], attribute_subsets)

    direct_result = attribute_information_gain(
        0.9402859586706309, 14, attribute_subsets
    )

    assert collection_result == direct_result
    snapshot.assert_match(collection_result)
