import os
import sys
import shutil
from pathlib import Path

from generate_page import generate_page

PUBLIC_DIR = "docs"  # Changed from "public" to "docs"
STATIC_DIR = "static"
CONTENT_DIR = "content"

def clean_public_directory():
    """Delete everything in the docs directory."""
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

def copy_content_files(basepath):
    """Convert all markdown files from CONTENT_DIR to HTML in PUBLIC_DIR."""
    if os.path.exists(CONTENT_DIR):
        for root, dirs, files in os.walk(CONTENT_DIR):
            # Get relative path from CONTENT_DIR
            rel_path = os.path.relpath(root, CONTENT_DIR)
            
            # Create corresponding directory in PUBLIC_DIR if needed
            if rel_path != '.':
                os.makedirs(os.path.join(PUBLIC_DIR, rel_path), exist_ok=True)
            
            # Process markdown files
            for file in files:
                if file.endswith('.md'):
                    source_path = os.path.join(root, file)
                    
                    # Determine output path, converting .md to .html
                    output_filename = 'index.html' if file == 'index.md' else file.replace('.md', '.html')
                    
                    if rel_path == '.':
                        output_path = os.path.join(PUBLIC_DIR, output_filename)
                    else:
                        output_path = os.path.join(PUBLIC_DIR, rel_path, output_filename)
                    
                    # Generate the HTML page with basepath
                    generate_page(source_path, "template.html", output_path, basepath)

def main():
    # Get basepath from CLI argument or default to '/'
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    
    clean_public_directory()
    copy_static_files()
    copy_content_files(basepath)
    
    # Generate homepage with basepath
    generate_page(f"{CONTENT_DIR}/index.md", "template.html", f"{PUBLIC_DIR}/index.html", basepath)

if __name__ == "__main__":
    main()

