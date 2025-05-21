import unittest

from main import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK, "http://localhost")
        node4 = TextNode("This is a text node", TextType.LINK, "http://localhost")

        self.assertEqual(node, node2)
        self.assertEqual(node4, node3)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        node3 = TextNode("This is a text node", TextType.LINK)
        node4 = TextNode("This is a text node", TextType.LINK, "http://localhost")

        self.assertNotEqual(node, node2)
        self.assertNotEqual(node3, node4)

class TestConvertTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img(self):
        node = TextNode("This is a nice image", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props_to_html(), " src=\"https://www.google.com\" alt=\"This is a nice image\"")
        self.assertEqual(html_node.value, "")

    def test_code(self):
        node = TextNode("print(\"super secret code\")", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print(\"super secret code\")")


if __name__ == '__main__':
    unittest.main()
