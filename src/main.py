from textnode import TextNode, TextType


def main():
    new_textnode = TextNode(
        "this is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(new_textnode)


if __name__ == "__main__":
    main()
