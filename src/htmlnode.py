from textnode import TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        return ' '.join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
                f"children={self.children!r}, props={self.props!r})")

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have children.")
        
        # Generate the HTML for each child node recursively
        children_html = ''.join(child.to_html() for child in self.children)
        props = self.props_to_html()
        if props:
            return f"<{self.tag} {props}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag!r}, children={self.children!r}, props={self.props!r})"

def text_node_to_html_node(text_node):
    """
    Converts a TextNode into a LeafNode based on the TextType.
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        # For LINK type, we assume `text_node.text` is the anchor text and the URL is passed as props
        return LeafNode("a", text_node.text, {"href": text_node.text})
    
    elif text_node.text_type == TextType.IMAGE:
        # For IMAGE type, we assume `text_node.text` contains the image URL and `alt` text
        return LeafNode("img", "", {"src": text_node.text, "alt": text_node.text})
    
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")
