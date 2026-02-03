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

        original_text = node.text
        images = extract_markdown_images(original_text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image_alt, image_link in images:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)

            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    pass
