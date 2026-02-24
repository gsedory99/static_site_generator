from extract_title import extract_title
from markdown_to_html import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown_content = file.read()
    with open(template_path, "r") as f:
        template_content = f.read()

    html = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)
