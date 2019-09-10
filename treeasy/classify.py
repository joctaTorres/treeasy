from typing import Dict

from treeasy.types import Tree


def classify(tree: Tree, instance: Dict):
    model = tree.get_tree_dict()

    while True:
        tree_node = model["node"]

        if "values" in model.keys():
            instance_value = instance[tree_node]
            model = model["values"][instance_value]
        else:
            return tree_node
