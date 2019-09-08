from typing import List, Tuple

class Tree():
    def __init__(self, root:str):
        self.root = root
    
    def set_children(self, children:List[Tuple[str, "Tree"]]):
        for child in children:
            self.children.update(
                {
                    child[0] : child[1]
                }
            )
        


