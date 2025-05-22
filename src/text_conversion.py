from enum import Enum
from split import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(block_text):
    if ("#" in block_text[0:1]):
        return BlockType.HEADING
    if block_text.startswith("```") and block_text.endswith('```'):
        return BlockType.CODE
    block_text_by_line = block_text.split("\n")
    block_filtered = list(filter(
        lambda x: not x.startswith('-'),
        block_text_by_line))
    if len(block_filtered) == 0:
        return BlockType.UNORDERED_LIST
    block_filtered = list(filter(
        lambda x: not x.startswith('>'),
        block_text_by_line))
    if len(block_filtered) == 0:
        return BlockType.QUOTE
    check_ordered = True
    for i in range(len(block_text_by_line)):
        position = i + 1
        if not block_text_by_line[i].startswith(f"{position}."):
            check_ordered = False
            break
    if check_ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_textnodes(text):
    return split_nodes_link(
            split_nodes_image(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            [TextNode(text, TextType.TEXT)], "**", TextType.BOLD),
                    "_", TextType.ITALIC),
                "`", TextType.CODE)))

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(
        filter(
            lambda x: x != "",
            map(
                lambda x: x.strip(),
                blocks
            )
        )
    )
