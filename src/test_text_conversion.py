import unittest

from text_conversion import BlockType, block_to_block_type, markdown_to_blocks, text_to_textnodes
from textnode import TextNode, TextType

class TestTextToNode(unittest.TestCase):
    def test_simple_markdown(self):
        markdown = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        text_nodes = text_to_textnodes(markdown)

        self.assertListEqual(
            text_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ])

    def test_two_bold_markdown(self):
        markdown = "This is **text** and this **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        text_nodes = text_to_textnodes(markdown)

        self.assertListEqual(
            text_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD), TextNode(" and this ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ])

    def test_two_images_and_two_italic(self):
        markdown = "This is _text_ and this **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) with this ![image 2](https://localhost.com)"

        text_nodes = text_to_textnodes(markdown)

        self.assertListEqual(
            text_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.ITALIC),
                TextNode(" and this ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" with this ", TextType.TEXT),
                TextNode("image 2", TextType.IMAGE, "https://localhost.com"),
            ])

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_double_spaced(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here

This is the same paragraph on a new line


- This is a list
- with items


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here",
                "This is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_block_paragraph(self):
        block = "This is **bolded** paragraph"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH)

    def test_block_code(self):
        block = "```py\nprint(\"Very awesome code\")\n```"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE)

    def test_block_heading(self):
        block = "# Heading 1"
        block2 = "### Heading 3"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING)
        self.assertEqual(
            block_to_block_type(block2),
            BlockType.HEADING)

    def test_block_list(self):
        block = "- First Item\n- Second Item\n- Third Item"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST)

    def test_block_list_wrong(self):
        block = "- First Item\nSecond Item\n- Third Item"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH)

    def test_block_quote(self):
        block = "> First Quote\n> Second Quote\n> Third Quote"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE)

    def test_block_wrong(self):
        block = "> First Quote\n> Second Quote\nThird Quote"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH)

    def test_block_ordered(self):
        block = "1. First Order\n2. Second Order\n3. Third Order"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST)

    def test_block_ordered_wrong(self):
        block = "First Order\n2. Second Order\n3. Third Order"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH)


