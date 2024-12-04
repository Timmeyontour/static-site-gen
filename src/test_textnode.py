import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print(" ----- starting textnode tests ----- ")
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

        node9 = TextNode("This is a text node", TextType.CODE)
        print(text_node_to_html_node(node9))
        #self.assertEqual(text_node_to_html_node(node9), "LeafNode('None', This is a text node, None, None)")

if __name__ == "__main__":
    unittest.main()