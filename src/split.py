import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text):
    regex = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        splited_text = node.text.split(delimiter)
        if len(splited_text) % 2 == 0:
            raise ValueError("invalid markdown, delimiter not closed")
        split_nodes = []
        for i in range(len(splited_text)):
            if splited_text[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splited_text[i].replace("\n", " "), TextType.TEXT))
            else:
                split_nodes.append(TextNode(splited_text[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_with_func(old_nodes, func_with_extract, text_type):
    new_nodes = []
    for node in old_nodes:
        matches = func_with_extract(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        split_nodes = []
        original_text = node.text
        for match in matches:
            splited_text = original_text.split(f"[{match[0]}]({match[1]})", 1)
            if text_type == TextType.IMAGE:
                splited_text = original_text.split(f"![{match[0]}]({match[1]})", 1)
            split_nodes.append(TextNode(splited_text[0], TextType.TEXT))
            split_nodes.append(TextNode(match[0], text_type, match[1]))
            original_text = splited_text[1]
        if original_text != "":
            split_nodes.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes_with_func(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_with_func(old_nodes, extract_markdown_links, TextType.LINK)

