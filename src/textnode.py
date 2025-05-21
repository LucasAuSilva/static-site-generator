from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not self.text == other.text:
            return False
        if not self.text_type == other.text_type:
            return False
        if not self.url == other.url:
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(text_node.text, "b")
        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        case TextType.CODE:
            return LeafNode(text_node.text, "code")
        case TextType.LINK:
            props = { "href": text_node.url }
            return LeafNode(text_node.text, "a", props)
        case TextType.IMAGE:
            props = { "src": text_node.url, "alt": text_node.text }
            return LeafNode("", "img", props)
        case _:
            raise Exception(f"invalid text type: {text_node.text_type}")
