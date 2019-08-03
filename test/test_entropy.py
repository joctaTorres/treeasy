from unittest.mock import call, patch

from treeasy.entropy import collection_entropy, entropy


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
