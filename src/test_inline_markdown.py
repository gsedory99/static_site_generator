import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold_simple(self):
        node = TextNode("This is **bold** text", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" text", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )
