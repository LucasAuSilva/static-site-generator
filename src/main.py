import os
import sys
import shutil
from gen_content import copy_to_public, generate_page_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "template.html"


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_to_public(dir_path_static, dir_path_public)
    generate_page_recursive(
        basepath,
        dir_path_content,
        template_path,
        dir_path_public
    )


main()
