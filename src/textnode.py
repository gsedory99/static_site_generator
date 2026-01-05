from enum import Enum
import htmlnode


class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return (
            self.text == text_node.text
            and self.text_type == text_node.text_type
            and self.url == text_node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.PLAIN_TEXT:
        return htmlnode.LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return htmlnode.LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return htmlnode.LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE_TEXT:
        return htmlnode.LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return htmlnode.LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return htmlnode.LeafNode(
            "img",
            None,
            props={
                "src": text_node.url,
                "alt": text_node.text,
            },
        )
    else:
        raise Exception
