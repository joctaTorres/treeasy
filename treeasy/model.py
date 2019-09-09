class Tree:
    def __init__(self, root_name):
        self.root = root_name
        self.children = []
    
    def set_children(self, children):
        self.children = children
    
    def __str__(self):
        string = f"({self.root})"
        for child in self.children:
            child_str = str(child[1])
            string += f"\n\t| [{child[0]}] : {child_str}"
        
        return string
    

