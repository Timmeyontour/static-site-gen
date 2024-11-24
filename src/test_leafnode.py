import unittest

from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
        assert node.to_html() == "<p>This is a paragraph of text.</p>"  # Passes

if __name__ == "__main__":
    unittest.main()