import pandas as pd

from treeasy.trees import treeID3


def test_tree_id3(snapshot):
    training_data = pd.read_csv("./datasets/tennis.csv")
    training_data.drop(["day"], axis=1, inplace=True)

    attributes = list(training_data.columns)
    target = "play"

    expected_tree = treeID3(training_data, target, attributes)
    snapshot.assert_match(str(expected_tree))
