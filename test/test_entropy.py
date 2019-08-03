import pytest

from treeasy.entropy import entropy

def test_entropy(snapshot):
    snapshot.assert_match(entropy([(9/14), (5/14)]))
    snapshot.assert_match(entropy([0.5, 0.2, 0.1, 0.1, 0.1]))
