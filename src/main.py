from htmlnode import LeafNode
from textnode import TextType, TextNode

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
            raise Exception("No text type exists with this value")

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(dummy)

main()
