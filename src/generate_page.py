import os
from pathlib import Path

from extract_title import extract_title
from markdown_to_html import markdown_to_html_node


def generate_pages_recursive(
    dir_path_content, template_path, dest_dir_path, basepath=""
):
    for item in os.listdir(dir_path_content):
        src_path = Path(dir_path_content) / item
        dst_path = Path(dest_dir_path) / item
        # src_path = os.path.join(dir_path_content, item)
        # dst_path = os.path.join(dest_dir_path, item)
        # src_path = Path(src_path).with_suffix(".html")
        if os.path.isfile(src_path):
            print(
                f"Generating Page from {src_path} to {dst_path} using {template_path}"
            )
            with open(src_path, "r") as f:
                markdown_content = f.read()
            with open(template_path, "r") as f2:
                template_content = f2.read()

            html = markdown_to_html_node(markdown_content).to_html()
            title = extract_title(markdown_content)

            template_content = template_content.replace("{{ Title }}", title)
            template_content = template_content.replace("{{ Content }}", html)
            template_content = template_content.replace('href="/', f'href="{basepath}')
            template_content = template_content.replace('src="/', f'src="{basepath}')

            dst_path = dst_path.with_suffix(".html")
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)

            with open(dst_path, "w") as f3:
                f3.write(template_content)

        elif os.path.isdir(src_path):
            os.makedirs(dst_path, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dst_path, basepath)
