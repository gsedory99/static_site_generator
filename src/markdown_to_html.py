from htmlnode import HTML_Node, LeafNode, ParentNode
from markdown_to_blocks import BlockType, block_to_block_type, markdown_to_blocks
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            html_nodes.append(heading_node_creator(block))
        elif block_type == BlockType.UNORDERED_LIST:
            html_nodes.append(unordered_list_node_creator(block))
        elif block_type == BlockType.ORDERED_LIST:
            html_nodes.append(ordered_list_node_creator(block))
        elif block_type == BlockType.CODE:
            html_nodes.append(code_node_creator(block))
        elif block_type == BlockType.PARAGRAPH:
            html_nodes.append(paragraph_node_creator(block))
        elif block_type == BlockType.QUOTE:
            html_nodes.append(quote_node_creator(block))
    return ParentNode("div", html_nodes)


def heading_node_creator(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    tag = f"h{count}"

    children_nodes = text_to_children(block[count + 1 :])
    return ParentNode(tag, children_nodes)


def unordered_list_node_creator(block):
    block_lines = block.split("\n")
    html_items = []
    for block_line in block_lines:
        children_nodes = text_to_children(block_line[2:])
        html_items.append(ParentNode("li", children_nodes))
    return ParentNode("ul", html_items)


def ordered_list_node_creator(block):
    block_lines = block.split("\n")
    html_items = []
    for block_line in block_lines:
        children_nodes = text_to_children(block_line.split(". ", 1)[1])
        html_items.append(ParentNode("li", children_nodes))
    return ParentNode("ol", html_items)


def quote_node_creator(block):
    block_lines = block.splitlines()
    cleaned_block_lines = [
        line.lstrip(">").strip() for line in block_lines if line.lstrip(">").strip()
    ]
    new_block_string = " ".join(cleaned_block_lines)
    children = text_to_children(new_block_string)
    return ParentNode("blockquote", children)


def code_node_creator(block):
    block = block[4:-3]
    block_html_node = text_node_to_html_node(TextNode(block, TextType.PLAIN_TEXT))
    return ParentNode("pre", [ParentNode("code", [block_html_node])])


def paragraph_node_creator(block):
    blocks = block.split("\n")
    block = [block.strip() for block in blocks if block.strip()]
    joined_block = " ".join(block)
    children_nodes = text_to_children(joined_block)
    return ParentNode("p", children_nodes)
