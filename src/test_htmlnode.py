import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_filled(self):
        props = { "href": "https://www.google.com", "target": "_blank" }
        node = HTMLNode("a", "link", None, props)

        props_text = node.props_to_html()

        self.assertEqual(props_text, "href=\"https://www.google.com\" target=\"_blank\"")

    def test_props_to_html_not_filled(self):
        node = HTMLNode("a", "link")

        props_text = node.props_to_html()

        self.assertEqual(props_text, "")

    def test_html_repr(self):
        node = HTMLNode("a", "link")
        props = { "href": "https://www.google.com", "target": "_blank" }
        node2 = HTMLNode("a", "link 2", None, props)

        props_text = f"{node}"
        props_text2 = f"{node2}"

        self.assertEqual(props_text, "<a> link </a>\nprops: None\nchildren: None")
        self.assertEqual(props_text2, f"<a> link 2 </a>\nprops: {props}\nchildren: None")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_with_tag(self):
        node = LeafNode("Hello, World!", "p")
        node2 = LeafNode("World", "b")

        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")
        self.assertEqual(node2.to_html(), "<b>World</b>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode("World")

        self.assertEqual(node.to_html(), "World")

