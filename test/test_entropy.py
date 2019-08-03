import pytest
from unittest.mock import patch, call

from treeasy.entropy import entropy, collection_entropy

def test_entropy(snapshot):
    snapshot.assert_match(entropy([(9/14), (5/14)]))
    snapshot.assert_match(entropy([0.5, 0.2, 0.1, 0.1, 0.1]))


@patch("treeasy.entropy.entropy")
def test_collection_entropy_call(entropy, snapshot):
    collection_entropy([9, 5])
    collection_entropy([7, 9, 4])

    entropy.assert_has_calls(
        [
            call([(9/14), (5/14)]),
            call([(7/20), (9/20), (4/20)])
        ]
    )


