import pandas as pd

from treeasy.classify import classify
from treeasy.trees import tree_id3


def test_classify_tree_id3():
    training_data = pd.read_csv("./datasets/tennis.csv")
    training_data.drop(["day"], axis=1, inplace=True)

    attributes = list(training_data.columns)
    target = "play"

    tree = tree_id3(training_data, target, attributes)

    instance_no = {
        "outlook": "Sunny",
        "temp": "Hot",
        "humidity": "High",
        "wind": "Weak",
    }

    instance_yes = {
        "outlook": "Overcast",
        "temp": "Hot",
        "humidity": "High",
        "wind": "Weak",
    }

    result_no = classify(tree, instance_no)
    result_yes = classify(tree, instance_yes)

    assert result_no == "No"
    assert result_yes == "Yes"
