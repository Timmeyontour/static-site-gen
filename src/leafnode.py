import htmlnode

'''
A LeafNode is a type of HTMLNode that represents a single HTML tag with no children. 
'''

class LeafNode(htmlnode.HTMLNode):
    def __init__(self, tag, value, props=None):
        
        super().__init__(tag, value, None, props)

    '''
    LeafNode("p", "This is a paragraph of text.")
    LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    Should render as:

    <p>This is a paragraph of text.</p>
    <a href="https://www.google.com">Click me!</a>
    '''

    def to_html(self):
        if self.value is None:
            raise ValueError("Cannot render LeafNode without a value.")
        
        if self.tag is None:
            return str(self.value)  # Return raw text if no tag is provided.
        
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"