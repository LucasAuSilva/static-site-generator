import unittest

from htmlnode import HTMLNode

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

