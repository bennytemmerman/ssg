from textnode import TextNode, TextType
import os
import shutil

def copy_directory(src, dest):
    # Ensure destination exists, otherwise create it
    if os.path.exists(dest):
        shutil.rmtree(dest)  # Delete existing contents
    os.makedirs(dest)
    
    # Iterate through all files and subdirectories in source
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        
        if os.path.isdir(src_path):
            copy_directory(src_path, dest_path)  # Recursive call for directories
        else:
            shutil.copy(src_path, dest_path)  # Copy files
            print(f"Copied: {src_path} -> {dest_path}")

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    src = "static"
    dest = "public"
    copy_directory(src, dest)
    print("Copy completed successfully.")

main()
