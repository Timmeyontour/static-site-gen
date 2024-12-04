import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        print(" ----- starting leafnode tests ----- ")

        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
        self.assertIsInstance(node2, LeafNode)
        assert node2.to_html() == '<a href="https://www.google.com">Click me!</a>' # Passes
        
        node3 = LeafNode(None, None, {"href": "https://www.google.com"})

        # accessing the error after the test
        with self.assertRaises(ValueError) as val_error:
            node3.to_html()

        exception = val_error.exception
        print(f"this is the {repr(exception)}")

        with self.assertRaises(ValueError) :
            print("ok")
            node3.to_html()

        node4 = LeafNode(None, "This is a paragraph of text.", {"href": "https://www.google.com"})
        self.assertEqual(node4.to_html(), 'This is a paragraph of text.')

        node5 = LeafNode("p", "This is a paragraph of text.")
        node6 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node5, node6)
        self.assertIsNot(node5, node6)

if __name__ == "__main__":
    unittest.main()