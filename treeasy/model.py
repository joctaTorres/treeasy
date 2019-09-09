import json

class Tree:
    def __init__(self, root_name):
        self.root = root_name
        self.children = []
    
    def set_children(self, children):
        self.children = children
    
    def get_tree_dict(self):
        tree_dict = {
            "node": self.root,
        }

        if len(self.children) > 0:
            tree_dict.update(
                { "values" : {v : cd.get_tree_dict() for v, cd in self.children } }
            )
        
        return tree_dict
    
    def __str__(self):

        return json.dumps(self.get_tree_dict())
    

