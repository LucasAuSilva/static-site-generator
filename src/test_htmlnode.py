import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_filled(self):
        props = { "href": "https://www.google.com", "target": "_blank" }
        node = HTMLNode("a", "link", None, props)

        props_text = node.props_to_html()

        self.assertEqual(props_text, " href=\"https://www.google.com\" target=\"_blank\"")

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_leaf(self):
        node = ParentNode("p", [
            LeafNode("Bold text", "b"),
            LeafNode("Normal text", None),
            LeafNode("italic text", "i"),
            LeafNode("Normal text", None),
        ])
        html = node.to_html()
        self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_parent_and_leaf(self):
        node_inside = ParentNode("div", [
            LeafNode("Normal text", "p")
        ])
        node = ParentNode("body", [
            node_inside
        ])
        html = node.to_html()
        self.assertEqual(html, "<body><div><p>Normal text</p></div></body>")

    def test_to_html_with_leaf_with_props(self):
        props = { "style": "text-align:right", "id": "paragraph" }
        node = ParentNode("p", [
            LeafNode("Bold text", "b"),
            LeafNode("Normal text", None),
            LeafNode("italic text", "i"),
            LeafNode("Normal text", None),
        ], props)
        html = node.to_html()
        self.assertEqual(html, "<p style=\"text-align:right\" id=\"paragraph\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_parent_and_leaf_with_props(self):
        props_div = { "class": "div-text" }
        props_body = { "class": "body-page" }
        node_inside = ParentNode("div", [
            LeafNode("Normal text", "p")
        ], props_div)
        node = ParentNode("body", [
            node_inside
        ], props_body)
        html = node.to_html()
        self.assertEqual(html, "<body class=\"body-page\"><div class=\"div-text\"><p>Normal text</p></div></body>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

