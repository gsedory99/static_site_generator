from copy_to_public import copy_static
from generate_page import generate_pages_recursive


def main():  # Test the new text_to_textnodes function

    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
