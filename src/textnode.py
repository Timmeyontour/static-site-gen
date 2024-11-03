from enum import Enum

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