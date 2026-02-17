import htmlnode
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes


def main():
    # Test the new text_to_textnodes function
    test_text = "This is **bold** and *italic* and `code` text with an ![image](https://example.com/image.png) and a [link](https://example.com)"
    nodes = text_to_textnodes(test_text)

    print("Parsed nodes:")
    for node in nodes:
        print(node)

    # Test with a simple case
    simple_text = "This is plain text"
    simple_nodes = text_to_textnodes(simple_text)
    print("\nSimple case:")
    for node in simple_nodes:
        print(node)


if __name__ == "__main__":
    main()
