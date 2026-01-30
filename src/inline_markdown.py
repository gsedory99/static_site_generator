from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        split_text_list = node.text.split(delimiter)
        if len(split_text_list) % 2 == 0:
            raise Exception("This is not valid Markdown")
        for i in range(len(split_text_list)):
            if split_text_list[i] == "":
                continue
            elif i % 2 == 0:
                new_nodes.append(TextNode(split_text_list[i], TextType.PLAIN_TEXT))
            else:
                new_nodes.append(TextNode(split_text_list[i], text_type))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        image_info = extract_markdown_images(node.text)
        sections = node.text.split(f"![{image_info[0]}]({image_info[1]})", 1)
        text_node_build = []


def split_nodes_link(old_nodes):
    pass
