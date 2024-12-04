import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        print(" ----- starting parentnode tests ----- ")
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        node2 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node, node2)

        with self.assertRaises(TypeError) as type_error:
            node3 = ParentNode(("a", None, {"href": "https://www.google.com"}))
        exception = type_error.exception
        print(f"this is the {repr(exception)}")

        node4 = ParentNode("p",  [LeafNode("b", "Bold text")], {"href": "https://www.google.com"})
        
        # test for nested parent nodes

if __name__ == "__main__":
    unittest.main()