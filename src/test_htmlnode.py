import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        print("starting htmlnode tests")
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

        # accessing the error after the test
        with self.assertRaises(ValueError) as val_error:
            node2.props_to_html()

        exception = val_error.exception
        print(f"this is the {repr(exception)}")

        with self.assertRaises(NotImplementedError) :
            print("ok")
            node.to_html()
            

if __name__ == "__main__":
    unittest.main()