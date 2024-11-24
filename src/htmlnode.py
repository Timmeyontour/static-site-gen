
'''
The HTMLNode class will represent a "node" in an HTML document tree (like a <p> tag and its contents, 
or an <a> tag and its contents) and is purpose-built to render itself as HTML.

Perhaps counterintuitively, every data member should be optional and default to None:
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
'''

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag   
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def props_to_html(self):
        result = ""
        if self.props != None:
            for key in self.props:
                    result += f'{key}="{self.props[key]}" '
            if result.endswith(" "):
                result = result[:-1]
            return result
        else:
            raise ValueError
    
    def __repr__(self):
      return f"HTMLNode('{self.tag}', {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        # Get all attributes of obj1 (except for methods and private attributes)
        
        attrs = [attr for attr in dir(self) if not attr.startswith("__") and not callable(getattr(self, attr))]
        
        # Check each attribute's value in both objects
        for attr in attrs:
            if getattr(self, attr) != getattr(other, attr):
                return False  # Found a mismatch, so return False immediately
        return True  # All properties matched

        
