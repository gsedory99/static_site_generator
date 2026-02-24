import sys

from copy_to_public import copy_static
from generate_page import generate_pages_recursive


def main():  # Test the new text_to_textnodes function
    copy_static("static", "docs")
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        generate_pages_recursive(
            basepath + "content", "template.html", basepath + "docs"
        )
    generate_pages_recursive("content", "template.html", "docs")


if __name__ == "__main__":
    main()
