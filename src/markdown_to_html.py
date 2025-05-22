
from htmlnode import LeafNode, ParentNode
from text_conversion import BlockType, block_to_block_type, markdown_to_blocks, text_to_textnodes
from textnode import text_node_to_html_node

def extract_title(markdown):
    first_line = markdown.split("\n\n")[0].strip()
    if not first_line.startswith("# "):
        raise Exception("First line need to be title of page")
    return first_line[2:]

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    block_html_nodes = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        html_node = convert_block_type_to_html(block, block_type)
        block_html_nodes.append(html_node)
    return ParentNode("div", block_html_nodes)

def convert_list_item_to_html(item):
    text_nodes = text_to_textnodes(item)
    html_nodes = list(map(
                      text_node_to_html_node,
                      text_nodes))
    return ParentNode("li", html_nodes)

def convert_block_type_to_html(block, block_type):
    match (block_type):
        case BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            html_nodes = list(map(
                              text_node_to_html_node,
                              text_nodes))
            return ParentNode("p", html_nodes)
        case BlockType.HEADING:
            heading_number = len(block.split(" ")[0])
            return LeafNode(block.replace("#", "")[1:], f"h{heading_number}")
        case BlockType.QUOTE:
            return LeafNode(block.replace("> ", "").replace("\n", " "), "blockquote")
        case BlockType.UNORDERED_LIST:
            html_list = list(
                map(
                    lambda x: convert_list_item_to_html(x.replace("- ", "")),
                    block.split("\n")
                )
            )
            return ParentNode("ul", html_list)
        case BlockType.ORDERED_LIST:
            html_list = list(
                map(
                    lambda x: convert_list_item_to_html(x[3:]),
                    block.split("\n")
                )
            )
            return ParentNode("ol", html_list)
        case BlockType.CODE:
            text_clean = block.replace("```", "")
            return ParentNode("pre", [LeafNode(text_clean, "code")])
