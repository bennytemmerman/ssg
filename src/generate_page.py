import os
from pathlib import Path
from markdown_blocks import *
from extract_title import *

def generate_page(from_path, template_path, dest_path, basepath):
    # Print the generation message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, "r", encoding="utf-8") as markdown_file:
        markdown_content = markdown_file.read()

    # Read the template file
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Convert markdown to HTML (assuming markdown_to_html_node is defined elsewhere)
    html_content = markdown_to_html_node(markdown_content).to_html()

    # Extract the title from the markdown
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Create directories if they don't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Adjust basepath for links
    page_html = page_html.replace('href="/', f'href="{basepath}')
    page_html = page_html.replace('src="/', f'src="{basepath}')

    # Write the final HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as html_file:
        html_file.write(full_html)
