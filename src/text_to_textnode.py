from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    """
    Convert a text string into a list of TextNode objects based on markdown syntax.

    Args:
        text (str): The input text to parse

    Returns:
        list: List of TextNode objects representing the parsed text
    """
    # Start with a single text node containing all the text
    nodes = [TextNode(text, TextType.PLAIN_TEXT)]

    # Split nodes by bold markdown (**text**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)

    # Split nodes by italic markdown (*text* or _text_)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)

    # Split nodes by code markdown (`text`)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)

    # Split nodes by images (![alt](src))
    nodes = split_nodes_image(nodes)

    # Split nodes by links ([text](url))
    nodes = split_nodes_link(nodes)

    return nodes
