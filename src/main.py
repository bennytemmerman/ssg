import os
import shutil
from pathlib import Path

from generate_page import generate_page

PUBLIC_DIR = "public"
STATIC_DIR = "static"
CONTENT_DIR = "content"

def clean_public_directory():
    """Delete everything in the public directory."""
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    os.makedirs(PUBLIC_DIR)

def copy_static_files():
    """Copy all static files from STATIC_DIR to PUBLIC_DIR without copying the root folder."""
    if os.path.exists(STATIC_DIR):
        for item in os.listdir(STATIC_DIR):  # Iterate over items inside STATIC_DIR
            src = os.path.join(STATIC_DIR, item)
            dst = os.path.join(PUBLIC_DIR, item)
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)  # Copy directories
            else:
                shutil.copy2(src, dst)  # Copy files

def main():
    clean_public_directory()
    copy_static_files()
    
    # Generate homepage
    generate_page(f"{CONTENT_DIR}/index.md", "template.html", f"{PUBLIC_DIR}/index.html")

if __name__ == "__main__":
    main()

