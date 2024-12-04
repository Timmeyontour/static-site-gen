from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "img"

'''
A "TextNode" is an intermediate representation between Markdown and HTML, and is specific to inline markup.
'''

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text   
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        # Get all attributes of obj1 (except for methods and private attributes)
        
        attrs = [attr for attr in dir(self) if not attr.startswith("__") and not callable(getattr(self, attr))]
        
        # Check each attribute's value in both objects
        for attr in attrs:
            if getattr(self, attr) != getattr(other, attr):
                return False  # Found a mismatch, so return False immediately
        return True  # All properties matched

        
    def __repr__(self):
      return f"TextNode('{self.text}', {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):

    match text_node.text_type:
        case "normal":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)

        case "italic":
            return LeafNode("i", text_node.text)

        case "code":
            return LeafNode("code", text_node.text)

        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case "img":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")