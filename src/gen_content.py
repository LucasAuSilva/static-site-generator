import os
from os.path import isfile
import shutil
from markdown_to_html import markdown_to_html_node,extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    template_file = open(template_path)
    template_contents = template_file.read()
    template_file.close()

    md_file = open(from_path, "r")
    md_contents = md_file.read()
    html = markdown_to_html_node(md_contents).to_html()
    page_title = extract_title(md_contents)
    new_page_contents = template_contents.replace("{{ Title }}", page_title).replace("{{ Content }}", html)
    md_file.close()

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    new_page = open(dest_path, 'w')
    new_page.write(new_page_contents)
    new_page.close()

def generate_page_recursive(path_content, template_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    for filename in os.listdir(path_content):
        from_path = os.path.join(path_content, filename)
        new_path = os.path.join(dest_path, filename)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, new_path.replace(".md", ".html"))
        else:
            generate_page_recursive(from_path, template_path, new_path)

def copy_to_public(src_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(src_dir_path):
        from_path = os.path.join(src_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_to_public(from_path, dest_path)
