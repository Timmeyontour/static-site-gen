import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.BOLD, "https://www.geeksforgeeks.org/comments-in-shell-script/")
        node4 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.NORMAL)
        node6 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node5, node6)

        node7 = TextNode("TThis is a text node", TextType.NORMAL)
        node8 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()