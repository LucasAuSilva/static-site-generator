from htmlnode import LeafNode
from textnode import TextType, TextNode

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(dummy)

main()
