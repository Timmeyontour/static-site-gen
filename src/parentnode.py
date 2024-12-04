import htmlnode

'''
The new ParentNode class will handle the nesting of HTML nodes inside of one another. 
Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.
'''

class ParentNode(htmlnode.HTMLNode):
    def __init__(self, tag, children, props=None):

        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Cannot use ParentNode without a tag.")
        
        if self.children is None:
            raise ValueError("Cannot use ParentNode without children.")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag} {self.props_to_html()}>{children_html}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"