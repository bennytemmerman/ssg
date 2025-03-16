from textnode import TextType, TextNode
import re

def split_nodes_delimiter(nodes, delimiter, text_type):
    new_nodes = []
    
    for node in nodes:
        parts = node.text.split(delimiter)

        # Ensure an odd number of parts (valid pairs of delimiters)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Regular text (outside delimiter)
                if part:
                    new_nodes.append(TextNode(part, node.text_type))
            else:
                # Formatted text (inside delimiter)
                if part:
                    # Make sure that the full word gets included when split by a delimiter
                    # Ensure no accidental splitting of words (like 'bold' into 'o' and 'ld')
                    new_nodes.append(TextNode(part, text_type))  

    return new_nodes

