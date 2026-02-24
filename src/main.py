from copy_to_public import copy_static
from generate_page import generate_page


def main():  # Test the new text_to_textnodes function

    copy_static("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
