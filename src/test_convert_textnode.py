import unittest
from convert_textnode import split_nodes_delimeter
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold_simple(self):
        node = TextNode("This is **bold** text", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" text", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )
