from textnode import TextNode, TextType


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
